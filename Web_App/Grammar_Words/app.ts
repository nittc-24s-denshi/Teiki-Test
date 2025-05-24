interface WordPair {
    word: string;
    japanese: string;
}

interface StudySession {
    words: WordPair[];
    currentIndex: number;
    correctCount: number;
    incorrectCount: number;
    mode: 'en-jp' | 'jp-en'; // 英語→日本語 or 日本語→英語
    showingAnswer: boolean;
}

interface AnswerLog {
    word: string;
    japanese: string;
    userAnswer: string;
    isCorrect: boolean;
}

class VocabularyApp {
    private session: StudySession;
    private allWords: WordPair[] = [];
    private answerLogs: AnswerLog[] = [];
    private studyType: 'flashcard' | 'multiple-choice' = 'flashcard';

    // DOM要素
    private elements = {
        loading: document.getElementById('loading') as HTMLElement,
        cardContainer: document.getElementById('cardContainer') as HTMLElement,
        wordType: document.getElementById('wordType') as HTMLElement,
        wordDisplay: document.getElementById('wordDisplay') as HTMLElement,
        answerType: document.getElementById('answerType') as HTMLElement,
        answerDisplay: document.getElementById('answerDisplay') as HTMLElement,
        cardFront: document.getElementById('cardFront') as HTMLElement,
        cardBack: document.getElementById('cardBack') as HTMLElement,
        showAnswerBtn: document.getElementById('showAnswerBtn') as HTMLElement,
        correctBtn: document.getElementById('correctBtn') as HTMLElement,
        incorrectBtn: document.getElementById('incorrectBtn') as HTMLElement,
        currentWord: document.getElementById('currentWord') as HTMLElement,
        totalWords: document.getElementById('totalWords') as HTMLElement,
        correctCount: document.getElementById('correctCount') as HTMLElement,
        incorrectCount: document.getElementById('incorrectCount') as HTMLElement,
        progressFill: document.getElementById('progressFill') as HTMLElement,
        modeToggle: document.getElementById('modeToggle') as HTMLElement,
        restartBtn: document.getElementById('restartBtn') as HTMLElement,
        shuffleBtn: document.getElementById('shuffleBtn') as HTMLElement,
        completionScreen: document.getElementById('completionScreen') as HTMLElement,
        finalAccuracy: document.getElementById('finalAccuracy') as HTMLElement,
        finalCorrect: document.getElementById('finalCorrect') as HTMLElement,
        finalTotal: document.getElementById('finalTotal') as HTMLElement,
        restartFinalBtn: document.getElementById('restartFinalBtn') as HTMLElement,
        wordCard: document.getElementById('wordCard') as HTMLElement,
        multipleChoice: document.getElementById('multipleChoice') as HTMLElement,
        mcWordType: document.getElementById('mcWordType') as HTMLElement,
        mcWordDisplay: document.getElementById('mcWordDisplay') as HTMLElement,
        mcOptions: document.getElementById('mcOptions') as HTMLElement,
        quizToggle: document.getElementById('quizToggle') as HTMLElement
    };

    constructor() {
        this.session = {
            words: [],
            currentIndex: 0,
            correctCount: 0,
            incorrectCount: 0,
            mode: 'en-jp',
            showingAnswer: false
        };

        this.init();
    }

    private async init(): Promise<void> {
        await this.loadWords();
        this.setupEventListeners();
        this.startNewSession();
    }

    private async loadWords(): Promise<void> {
        try {
            const response = await fetch('words.csv');
            const csvText = await response.text();
            
            const lines = csvText.trim().split('\n');
            const headers = lines[0].split(',');
            
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

    private setupEventListeners(): void {
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

    private startNewSession(): void {
        this.shuffleAllWords();
        this.session = {
            words: this.allWords.slice(0, 15),
            currentIndex: 0,
            correctCount: 0,
            incorrectCount: 0,
            mode: this.session.mode,
            showingAnswer: false
        };
        this.answerLogs = [];
        this.elements.loading.style.display = 'none';
        this.elements.cardContainer.style.display = 'block';
        this.elements.completionScreen.style.display = 'none';
        this.updateStats();
        this.showCurrentWord();
    }

    private shuffleAllWords(): void {
        for (let i = this.allWords.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.allWords[i], this.allWords[j]] = [this.allWords[j], this.allWords[i]];
        }
    }

    private shuffleWords(): void {
        this.shuffleAllWords();
        this.session.words = this.allWords.slice(0, 15);
        this.session.currentIndex = 0;
        this.showCurrentWord();
    }

    private toggleMode(): void {
        this.session.mode = this.session.mode === 'en-jp' ? 'jp-en' : 'en-jp';
        this.showCurrentWord();
    }

    private toggleStudyType(): void {
        if (this.studyType === 'flashcard') {
            this.studyType = 'multiple-choice';
            this.elements.quizToggle.textContent = 'フラッシュカードに切替';
        } else {
            this.studyType = 'flashcard';
            this.elements.quizToggle.textContent = '四択モードに切替';
        }
        this.showCurrentWord();
    }

    private showCurrentWord(): void {
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

    private renderMultipleChoice(currentWord: WordPair): void {
        const isEnToJp = this.session.mode === 'en-jp';
        this.elements.mcWordType.textContent = isEnToJp ? '英語 → 日本語' : '日本語 → 英語';
        this.elements.mcWordDisplay.textContent = isEnToJp ? currentWord.word : currentWord.japanese;

        const options: WordPair[] = [currentWord];
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
                    this.markAnswer(true);
                } else {
                    btn.classList.add('incorrect');
                    this.markAnswer(false);
                }
                Array.from(this.elements.mcOptions.children).forEach(b => (b as HTMLButtonElement).disabled = true);
            };
            this.elements.mcOptions.appendChild(btn);
        });
    }

    private showAnswer(): void {
        this.session.showingAnswer = true;
        this.elements.cardFront.style.display = 'none';
        this.elements.cardBack.style.display = 'block';
    }

    private markAnswer(isCorrect: boolean): void {
        if (this.studyType === 'flashcard' && !this.session.showingAnswer) return;

        const currentWord = this.session.words[this.session.currentIndex];
        let userAnswer = '';
        if (this.session.mode === 'en-jp') {
            userAnswer = this.elements.answerDisplay.textContent || '';
        } else {
            userAnswer = this.elements.answerDisplay.textContent || '';
        }
        this.answerLogs.push({
            word: currentWord.word,
            japanese: currentWord.japanese,
            userAnswer: userAnswer,
            isCorrect: isCorrect
        });

        if (isCorrect) {
            this.session.correctCount++;
        } else {
            this.session.incorrectCount++;
        }

        this.session.currentIndex++;
        this.showCurrentWord();
    }

    private updateStats(): void {
        const current = this.session.currentIndex + 1;
        const total = this.session.words.length;
        const progress = (this.session.currentIndex / total) * 100;

        this.elements.currentWord.textContent = current.toString();
        this.elements.totalWords.textContent = total.toString();
        this.elements.correctCount.textContent = this.session.correctCount.toString();
        this.elements.incorrectCount.textContent = this.session.incorrectCount.toString();
        this.elements.progressFill.style.width = `${progress}%`;
    }

    private showCompletionScreen(): void {
        this.elements.cardContainer.style.display = 'none';
        this.elements.completionScreen.style.display = 'block';

        const total = this.session.correctCount + this.session.incorrectCount;
        const accuracy = total > 0 ? Math.round((this.session.correctCount / total) * 100) : 0;

        this.elements.finalAccuracy.textContent = accuracy.toString();
        this.elements.finalCorrect.textContent = this.session.correctCount.toString();
        this.elements.finalTotal.textContent = total.toString();

        // 結果リストを表示
        const resultList = this.elements.completionScreen.querySelector('#resultList') as HTMLElement;
        resultList.innerHTML = '<h3>解答一覧</h3>';
        const table = document.createElement('table');
        table.style.width = '100%';
        table.style.background = 'rgba(255,255,255,0.9)';
        table.style.borderCollapse = 'collapse';
        table.innerHTML = `<tr><th>英語</th><th>日本語</th><th>あなたの回答</th><th>正誤</th></tr>`;
        this.answerLogs.forEach(log => {
            const tr = document.createElement('tr');
            tr.className = log.isCorrect ? 'correct-row' : 'incorrect-row';
            tr.innerHTML = `<td>${log.word}</td><td>${log.japanese}</td><td>${log.userAnswer}</td><td>${log.isCorrect ? '○' : '✗'}</td>`;
            table.appendChild(tr);
        });
        resultList.appendChild(table);
    }
}

// アプリケーション開始
document.addEventListener('DOMContentLoaded', () => {
    new VocabularyApp();
}); 