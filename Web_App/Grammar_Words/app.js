"use strict";
class VocabularyApp {
    constructor() {
        this.allWords = [];
        this.answerLogs = [];
        this.studyType = 'flashcard';
        this._answered = false;
        this.availableFiles = [
            'Grammar_words(前期中間).csv',
            'Oral-Lesson1-Vocabulary.csv',
            'Oral-Lesson2-Vocabulary.csv',
            'Oral-Lesson3-Vocabulary.csv',
            'Oral-Lesson4-Vocabulary.csv',
            'Oral-Lesson5-Vocabulary.csv'
        ];
        this.selectedFiles = [this.availableFiles[0]];
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
            quizToggle: document.getElementById('quizToggle'),
            themeToggleBtn: document.getElementById('themeToggleBtn'),
            wordFileCheckboxes: document.getElementById('wordFileCheckboxes'),
            allWordsCount: document.getElementById('allWordsCount'),
            quizCountInput: document.getElementById('quizCountInput')
        };
        this.session = {
            words: [],
            currentIndex: 0,
            correctCount: 0,
            incorrectCount: 0,
            mode: 'en-jp',
            showingAnswer: false
        };
        this.quizCount = parseInt(this.elements.quizCountInput.value, 10) || 15;
        this.init();
    }
    async init() {
        this.initFileCheckboxes();
        await this.loadWords();
        this.setupEventListeners();
        this.setupThemeToggle();
        this.startNewSession();
        this.elements.quizCountInput.addEventListener('change', () => {
            let val = parseInt(this.elements.quizCountInput.value, 10);
            if (isNaN(val) || val < 1) val = 1;
            if (val > this.allWords.length) val = this.allWords.length;
            this.quizCount = val;
            this.elements.quizCountInput.value = val;
            this.startNewSession();
        });
    }
    initFileCheckboxes() {
        const container = this.elements.wordFileCheckboxes;
        container.innerHTML = '';
        this.availableFiles.forEach(file => {
            const label = document.createElement('label');
            label.style.marginRight = '8px';
            label.style.color = 'white';
            label.style.fontWeight = 'normal';
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = file;
            checkbox.checked = this.selectedFiles.includes(file);
            checkbox.addEventListener('change', async () => {
                // 選択中のファイルを更新
                this.selectedFiles = Array.from(container.querySelectorAll('input[type=checkbox]:checked')).map(cb => cb.value);
                if (this.selectedFiles.length === 0) {
                    // 1つは必ず選択されているようにする
                    checkbox.checked = true;
                    this.selectedFiles = [file];
                    return;
                }
                this.elements.loading.style.display = 'block';
                this.elements.cardContainer.style.display = 'none';
                this.elements.completionScreen.style.display = 'none';
                await this.loadWords();
                this.startNewSession();
            });
            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(file));
            container.appendChild(label);
        });
    }
    async loadWords() {
        try {
            let allWords = [];
            for (const file of this.selectedFiles) {
                const response = await fetch(file);
                const csvText = await response.text();
                const lines = csvText.trim().split('\n');
                // 1行目はヘッダーとしてスキップ
                const fileWords = lines.slice(1).map(line => {
                    const [word, japanese] = line.split(',');
                    return {
                        word: word ? word.trim() : '',
                        japanese: japanese ? japanese.trim() : ''
                    };
                }).filter(pair => pair.word && pair.japanese);
                allWords = allWords.concat(fileWords);
            }
            this.allWords = allWords;
            this.updateAllWordsCount();
            if (this.elements.quizCountInput) {
                this.elements.quizCountInput.max = this.allWords.length;
                if (parseInt(this.elements.quizCountInput.value, 10) > this.allWords.length) {
                    this.elements.quizCountInput.value = this.allWords.length;
                    this.quizCount = this.allWords.length;
                }
            }
            console.log(`${this.allWords.length}個の単語を${this.selectedFiles.join(', ')}から読み込みました`);
        }
        catch (error) {
            console.error('単語の読み込みに失敗しました:', error);
            alert('単語ファイルの読み込みに失敗しました。');
        }
    }
    updateAllWordsCount() {
        if (this.elements.allWordsCount) {
            this.elements.allWordsCount.textContent = `全${this.allWords.length}問`;
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
        document.addEventListener('keydown', (e) => {
            if (this.studyType === 'flashcard') {
                if (e.key === ' ' || e.key === 'Enter') {
                    e.preventDefault();
                    if (!this.session.showingAnswer) {
                        this.showAnswer();
                    }
                }
                else if (e.key === 'ArrowRight' || e.key === '1') {
                    e.preventDefault();
                    if (this.session.showingAnswer) {
                        this.markAnswer(true);
                    }
                }
                else if (e.key === 'ArrowLeft' || e.key === '2') {
                    e.preventDefault();
                    if (this.session.showingAnswer) {
                        this.markAnswer(false);
                    }
                }
            }
        });
    }
    setupThemeToggle() {
        const btn = this.elements.themeToggleBtn;
        const body = document.body;
        // 初期状態
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            body.setAttribute('data-theme', savedTheme);
            this.updateThemeBtnText(savedTheme);
        } else {
            this.updateThemeBtnText(this.getCurrentTheme());
        }
        btn.addEventListener('click', () => {
            const current = this.getCurrentTheme();
            const next = current === 'dark' ? 'light' : 'dark';
            body.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            this.updateThemeBtnText(next);
        });
    }
    getCurrentTheme() {
        const body = document.body;
        if (body.getAttribute('data-theme')) {
            return body.getAttribute('data-theme');
        }
        // OS設定に従う
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }
    updateThemeBtnText(theme) {
        const btn = this.elements.themeToggleBtn;
        if (theme === 'dark') {
            btn.textContent = '☀️ ライトモード';
        } else {
            btn.textContent = '🌙 ダークモード';
        }
    }
    startNewSession() {
        this.shuffleAllWords();
        let count = this.quizCount;
        if (!count || count < 1) count = 1;
        if (count > this.allWords.length) count = this.allWords.length;
        this.session = {
            words: this.allWords.slice(0, count),
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
        this.updateAllWordsCount();
    }
    shuffleAllWords() {
        for (let i = this.allWords.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [this.allWords[i], this.allWords[j]] = [this.allWords[j], this.allWords[i]];
        }
    }
    shuffleWords() {
        this.shuffleAllWords();
        this.session.words = this.allWords.slice(0, 15);
        this.session.currentIndex = 0;
        this.showCurrentWord();
    }
    toggleMode() {
        this.session.mode = this.session.mode === 'en-jp' ? 'jp-en' : 'en-jp';
        this.showCurrentWord();
    }
    toggleStudyType() {
        if (this.studyType === 'flashcard') {
            this.studyType = 'multiple-choice';
            this.elements.quizToggle.textContent = 'フラッシュカードに切替';
        }
        else {
            this.studyType = 'flashcard';
            this.elements.quizToggle.textContent = '四択モードに切替';
        }
        this.showCurrentWord();
    }
    showCurrentWord() {
        if (this.session.currentIndex >= this.session.words.length) {
            this.showCompletionScreen();
            return;
        }
        const currentWord = this.session.words[this.session.currentIndex];
        this.session.showingAnswer = false;
        // すべての要素のdisplayを明示的にリセット
        this.elements.cardFront.style.display = 'none';
        this.elements.cardBack.style.display = 'none';
        this.elements.multipleChoice.style.display = 'none';
        if (this.studyType === 'flashcard') {
            this.elements.cardFront.style.display = 'block';
            this.elements.cardBack.style.display = 'none';
            this.elements.multipleChoice.style.display = 'none';
            if (this.session.mode === 'en-jp') {
                this.elements.wordType.textContent = '英語 → 日本語';
                this.elements.wordDisplay.textContent = currentWord.word;
                this.elements.answerType.textContent = '日本語';
                this.elements.answerDisplay.textContent = currentWord.japanese;
            }
            else {
                this.elements.wordType.textContent = '日本語 → 英語';
                this.elements.wordDisplay.textContent = currentWord.japanese;
                this.elements.answerType.textContent = '英語';
                this.elements.answerDisplay.textContent = currentWord.word;
            }
        }
        else {
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
        const pool = this.allWords.filter(w => {
            if (isEnToJp) {
                return w.japanese !== currentWord.japanese;
            } else {
                return w.word !== currentWord.word && w.japanese !== currentWord.japanese;
            }
        });
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
        this._answered = false;
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'mc-option-btn';
            btn.textContent = isEnToJp ? opt.japanese : opt.word;
            btn.disabled = false;
            btn.onclick = () => {
                if (this._answered) return;
                this._answered = true;
                Array.from(this.elements.mcOptions.children).forEach(b => b.disabled = true);
                const isCorrect = isEnToJp
                    ? (btn.textContent === currentWord.japanese)
                    : (btn.textContent === currentWord.word);
                if (isCorrect) {
                    btn.classList.add('correct');
                    this.markAnswer(true);
                } else {
                    btn.classList.add('incorrect');
                    this.markAnswer(false);
                }
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
        if (this.studyType === 'flashcard' && !this.session.showingAnswer)
            return;
        const currentWord = this.session.words[this.session.currentIndex];
        let userAnswer = '';
        if (this.session.mode === 'en-jp') {
            userAnswer = this.elements.answerDisplay.textContent || '';
        }
        else {
            userAnswer = this.elements.answerDisplay.textContent || '';
        }
        console.log('[markAnswer] isCorrect:', isCorrect, 'currentIndex:', this.session.currentIndex, 'currentWord:', currentWord);
        this.answerLogs.push({
            word: currentWord.word,
            japanese: currentWord.japanese,
            userAnswer: userAnswer,
            isCorrect: isCorrect
        });
        if (isCorrect) {
            this.session.correctCount++;
        }
        else {
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
        const resultList = this.elements.completionScreen.querySelector('#resultList');
        resultList.innerHTML = '<h3>解答一覧</h3>';
        const table = document.createElement('table');
        table.style.width = '100%';
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
document.addEventListener('DOMContentLoaded', () => {
    new VocabularyApp();
});
