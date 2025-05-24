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

class VocabularyApp {
    private session: StudySession;
    private allWords: WordPair[] = [];

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
        wordCard: document.getElementById('wordCard') as HTMLElement
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
            const response = await fetch('../2025/Grammar&Writing/単語テスト/words.csv');
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
        this.elements.restartBtn.addEventListener('click', () => this.startNewSession());
        this.elements.shuffleBtn.addEventListener('click', () => this.shuffleWords());
        this.elements.restartFinalBtn.addEventListener('click', () => this.startNewSession());

        // キーボードショートカット
        document.addEventListener('keydown', (e) => {
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
        });
    }

    private startNewSession(): void {
        this.session = {
            words: [...this.allWords],
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

    private shuffleWords(): void {
        for (let i = this.session.words.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.session.words[i], this.session.words[j]] = [this.session.words[j], this.session.words[i]];
        }
        this.session.currentIndex = 0;
        this.showCurrentWord();
    }

    private toggleMode(): void {
        this.session.mode = this.session.mode === 'en-jp' ? 'jp-en' : 'en-jp';
        this.showCurrentWord();
    }

    private showCurrentWord(): void {
        if (this.session.currentIndex >= this.session.words.length) {
            this.showCompletionScreen();
            return;
        }

        const currentWord = this.session.words[this.session.currentIndex];
        this.session.showingAnswer = false;

        // カードフリップアニメーション
        this.elements.wordCard.classList.add('card-flip');
        
        setTimeout(() => {
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

            this.elements.cardFront.style.display = 'block';
            this.elements.cardBack.style.display = 'none';
            
            this.updateStats();
            this.elements.wordCard.classList.remove('card-flip');
        }, 300);
    }

    private showAnswer(): void {
        this.session.showingAnswer = true;
        this.elements.cardFront.style.display = 'none';
        this.elements.cardBack.style.display = 'block';
    }

    private markAnswer(isCorrect: boolean): void {
        if (!this.session.showingAnswer) return;

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
    }
}

// アプリケーション開始
document.addEventListener('DOMContentLoaded', () => {
    new VocabularyApp();
}); 