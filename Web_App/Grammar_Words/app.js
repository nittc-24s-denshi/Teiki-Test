class VocabularyApp {
    constructor() {
        this.session = {
            words: [],
            currentIndex: 0,
            correctCount: 0,
            incorrectCount: 0,
            mode: 'en-jp',
            showingAnswer: false
        };
        this.allWords = [];
        this.studyType = 'flashcard'; // 'flashcard' or 'multiple-choice'

        // DOM要素
        this.elements = {
            loading: document.getElementById('loading'),
            cardContainer: document.getElementById('cardContainer'),
            wordType: document.getElementById('wordType'),
            wordDisplay: document.getElementById('wordDisplay'),
            answerType: document.getElementById('answerType'),
            answerDisplay: document.getElementById('answerDisplay'),
            cardFront: document.getElementById('cardFront'),
            cardBack: document.getElementById('cardBack'),
            showAnswerBtn: document.getElementById('showAnswerBtn'),
            correctBtn: document.getElementById('correctBtn'),
            incorrectBtn: document.getElementById('incorrectBtn'),
            currentWord: document.getElementById('currentWord'),
            totalWords: document.getElementById('totalWords'),
            correctCount: document.getElementById('correctCount'),
            incorrectCount: document.getElementById('incorrectCount'),
            progressFill: document.getElementById('progressFill'),
            modeToggle: document.getElementById('modeToggle'),
            restartBtn: document.getElementById('restartBtn'),
            shuffleBtn: document.getElementById('shuffleBtn'),
            completionScreen: document.getElementById('completionScreen'),
            finalAccuracy: document.getElementById('finalAccuracy'),
            finalCorrect: document.getElementById('finalCorrect'),
            finalTotal: document.getElementById('finalTotal'),
            restartFinalBtn: document.getElementById('restartFinalBtn'),
            wordCard: document.getElementById('wordCard'),
            multipleChoice: document.getElementById('multipleChoice'),
            mcWordType: document.getElementById('mcWordType'),
            mcWordDisplay: document.getElementById('mcWordDisplay'),
            mcOptions: document.getElementById('mcOptions'),
            quizToggle: document.getElementById('quizToggle')
        };

        this.init();
    }

    async init() {
        await this.loadWords();
        this.shuffleAllWords();
        this.setupEventListeners();
        this.startNewSession();
    }

    async loadWords() {
        try {
            const response = await fetch('words.csv');
            const csvText = await response.text();
            
            const lines = csvText.trim().split('\n');
            
            this.allWords = lines.slice(1).map(line => {
                const [word, japanese] = line.split(',');
                return {
                    word: word.trim(),
                    japanese: japanese.trim()
                };
            }).filter(pair => pair.word && pair.japanese);

            console.log(`${this.allWords.length}個の単語を読み込みました`);
        } catch (error) {
            console.error('単語の読み込みに失敗しました:', error);
            alert('単語ファイルの読み込みに失敗しました。');
        }
    }

    shuffleAllWords() {
        for (let i = this.allWords.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.allWords[i], this.allWords[j]] = [this.allWords[j], this.allWords[i]];
        }
    }

    setupEventListeners() {
        this.elements.showAnswerBtn.addEventListener('click', () => this.showAnswer());
        this.elements.correctBtn.addEventListener('click', () => this.markAnswer(true));
        this.elements.incorrectBtn.addEventListener('click', () => this.markAnswer(false));
        this.elements.modeToggle.addEventListener('click', () => this.toggleMode());
        this.elements.quizToggle.addEventListener('click', () => this.toggleStudyType());
        this.elements.restartBtn.addEventListener('click', () => this.startNewSession());
        this.elements.shuffleBtn.addEventListener('click', () => this.shuffleWords());
        this.elements.restartFinalBtn.addEventListener('click', () => this.startNewSession());

        // キーボードショートカット
        document.addEventListener('keydown', (e) => {
            if (this.studyType === 'flashcard') {
                if (e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    if (!this.session.showingAnswer) {
                        this.showAnswer();
                    }
                } else if (e.key === 'ArrowRight' || e.key === '1') {
                    e.preventDefault();
                    if (this.session.showingAnswer) {
                        this.markAnswer(true);
                    }
                } else if (e.key === 'ArrowLeft' || e.key === '2') {
                    e.preventDefault();
                    if (this.session.showingAnswer) {
                        this.markAnswer(false);
                    }
                }
            }
        });
    }

    toggleMode() {
        this.session.mode = this.session.mode === 'en-jp' ? 'jp-en' : 'en-jp';
        this.elements.modeToggle.textContent = this.session.mode === 'en-jp' ? '英語→日本語' : '日本語→英語';
        this.showCurrentWord();
    }

    toggleStudyType() {
        if (this.studyType === 'flashcard') {
            this.studyType = 'multiple-choice';
            this.elements.quizToggle.textContent = 'フラッシュカードに切替';
        } else {
            this.studyType = 'flashcard';
            this.elements.quizToggle.textContent = '四択モードに切替';
        }
        this.showCurrentWord();
    }

    startNewSession() {
        this.shuffleAllWords();
        this.session = {
            words: this.allWords.slice(0, 15),
            currentIndex: 0,
            correctCount: 0,
            incorrectCount: 0,
            mode: this.session.mode,
            showingAnswer: false
        };

        this.elements.loading.style.display = 'none';
        this.elements.cardContainer.style.display = 'block';
        this.elements.completionScreen.style.display = 'none';

        this.updateStats();
        this.showCurrentWord();
    }

    shuffleWords() {
        this.shuffleAllWords();
        this.session.words = this.allWords.slice(0, 15);
        this.session.currentIndex = 0;
        this.showCurrentWord();
    }

    showCurrentWord() {
        if (this.session.currentIndex >= this.session.words.length) {
            this.showCompletionScreen();
            return;
        }

        const currentWord = this.session.words[this.session.currentIndex];
        this.session.showingAnswer = false;

        // アニメーションなしで即時表示
        if (this.studyType === 'flashcard') {
            this.elements.cardFront.style.display = 'block';
            this.elements.cardBack.style.display = 'none';
            this.elements.multipleChoice.style.display = 'none';
            if (this.session.mode === 'en-jp') {
                this.elements.wordType.textContent = '英語 → 日本語';
                this.elements.wordDisplay.textContent = currentWord.word;
                this.elements.answerType.textContent = '日本語';
                this.elements.answerDisplay.textContent = currentWord.japanese;
            } else {
                this.elements.wordType.textContent = '日本語 → 英語';
                this.elements.wordDisplay.textContent = currentWord.japanese;
                this.elements.answerType.textContent = '英語';
                this.elements.answerDisplay.textContent = currentWord.word;
            }
        } else {
            this.elements.cardFront.style.display = 'none';
            this.elements.cardBack.style.display = 'none';
            this.elements.multipleChoice.style.display = 'flex';
            this.renderMultipleChoice(currentWord);
        }
        this.updateStats();
    }

    renderMultipleChoice(currentWord) {
        const isEnToJp = this.session.mode === 'en-jp';
        this.elements.mcWordType.textContent = isEnToJp ? '英語 → 日本語' : '日本語 → 英語';
        this.elements.mcWordDisplay.textContent = isEnToJp ? currentWord.word : currentWord.japanese;

        const options = [currentWord];
        const pool = this.allWords.filter(w => (isEnToJp ? w.japanese : w.word) !== (isEnToJp ? currentWord.japanese : currentWord.word));
        while (options.length < 4 && pool.length > 0) {
            const idx = Math.floor(Math.random() * pool.length);
            options.push(pool[idx]);
            pool.splice(idx, 1);
        }
        for (let i = options.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [options[i], options[j]] = [options[j], options[i]];
        }

        this.elements.mcOptions.innerHTML = '';
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'mc-option-btn';
            btn.textContent = isEnToJp ? opt.japanese : opt.word;
            btn.onclick = () => {
                if ((isEnToJp && opt.japanese === currentWord.japanese) || (!isEnToJp && opt.word === currentWord.word)) {
                    btn.classList.add('correct');
                    // 遅延なしで即時遷移
                    this.markAnswer(true);
                } else {
                    btn.classList.add('incorrect');
                    this.markAnswer(false);
                }
                Array.from(this.elements.mcOptions.children).forEach(b => b.disabled = true);
            };
            this.elements.mcOptions.appendChild(btn);
        });
    }

    showAnswer() {
        this.session.showingAnswer = true;
        this.elements.cardFront.style.display = 'none';
        this.elements.cardBack.style.display = 'block';
    }

    markAnswer(isCorrect) {
        if (this.studyType === 'flashcard' && !this.session.showingAnswer) return;

        if (isCorrect) {
            this.session.correctCount++;
        } else {
            this.session.incorrectCount++;
        }

        this.session.currentIndex++;
        this.showCurrentWord();
    }

    updateStats() {
        const current = this.session.currentIndex + 1;
        const total = this.session.words.length;
        const progress = (this.session.currentIndex / total) * 100;

        this.elements.currentWord.textContent = current.toString();
        this.elements.totalWords.textContent = total.toString();
        this.elements.correctCount.textContent = this.session.correctCount.toString();
        this.elements.incorrectCount.textContent = this.session.incorrectCount.toString();
        this.elements.progressFill.style.width = `${progress}%`;
    }

    showCompletionScreen() {
        this.elements.cardContainer.style.display = 'none';
        this.elements.completionScreen.style.display = 'block';

        const total = this.session.correctCount + this.session.incorrectCount;
        const accuracy = total > 0 ? Math.round((this.session.correctCount / total) * 100) : 0;

        this.elements.finalAccuracy.textContent = accuracy.toString();
        this.elements.finalCorrect.textContent = this.session.correctCount.toString();
        this.elements.finalTotal.textContent = total.toString();
    }
}

// アプリケーション開始
document.addEventListener('DOMContentLoaded', () => {
    new VocabularyApp();
}); 