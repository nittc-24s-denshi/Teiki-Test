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
        this.setupCsvFileInput();
        setTimeout(() => { initWordListEditor(); }, 0);
    }
    async init() {
        this.initFileCheckboxes();
        await this.loadWords();
        this.setupEventListeners();
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
            label.className = 'checkbox-container';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = file;
            checkbox.checked = this.selectedFiles.includes(file);

            const checkmark = document.createElement('span');
            checkmark.className = 'checkmark';

            const labelText = document.createElement('span');
            labelText.className = 'checkbox-label';
            labelText.textContent = file;

            checkbox.addEventListener('change', async () => {
                // 既存のイベントリスナー処理をここに保持
                this.selectedFiles = Array.from(container.querySelectorAll('input[type=checkbox]:checked')).map(cb => cb.value);
                if (this.selectedFiles.length === 0) {
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
            label.appendChild(checkmark);
            label.appendChild(labelText);
            container.appendChild(label);
        });
    }
    async loadWords() {
        try {
            let allWords = [];
            for (const file of this.selectedFiles) {
                let csvText;
                if (this._virtualFiles && this._virtualFiles[file]) {
                    csvText = this._virtualFiles[file];
                } else {
                    const response = await fetch(file);
                    csvText = await response.text();
                }
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
            // 入力欄やtextareaにフォーカスがある場合は何もしない
            const tag = document.activeElement.tagName.toLowerCase();
            if (tag === 'input' || tag === 'textarea') return;
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
        // 音声読み上げボタン
        const speakBtn = document.getElementById('speakWordBtn');
        if (speakBtn) {
            speakBtn.onclick = () => {
                const word = this.elements.wordDisplay.textContent.split(' ')[0];
                speakEnglish(word);
            };
        }
        const speakMcBtn = document.getElementById('speakMcWordBtn');
        if (speakMcBtn) {
            speakMcBtn.onclick = () => {
                const word = this.elements.mcWordDisplay.textContent.split(' ')[0];
                speakEnglish(word);
            };
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
        // 音声ボタン再登録
        setTimeout(() => {
            const speakBtn = document.getElementById('speakWordBtn');
            if (speakBtn) {
                speakBtn.onclick = () => {
                    const word = this.elements.wordDisplay.textContent.split(' ')[0];
                    speakEnglish(word);
                };
            }
            const speakMcBtn = document.getElementById('speakMcWordBtn');
            if (speakMcBtn) {
                speakMcBtn.onclick = () => {
                    const word = this.elements.mcWordDisplay.textContent.split(' ')[0];
                    speakEnglish(word);
                };
            }
        }, 0);
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
        // フィードバック用要素を用意
        let feedback = this.elements.multipleChoice.querySelector('.mc-feedback');
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'mc-feedback';
            feedback.style.fontSize = '1.3rem';
            feedback.style.fontWeight = 'bold';
            feedback.style.margin = '18px 0 0 0';
            feedback.style.minHeight = '2em';
            feedback.style.textAlign = 'center';
            this.elements.multipleChoice.appendChild(feedback);
        }
        feedback.textContent = '';
        let feedbackTimeout = null;
        // 単語部分クリックで次の問題へ進む
        this.elements.mcWordDisplay.onclick = () => {
            if (this._answered && feedback.textContent) {
                if (feedbackTimeout) clearTimeout(feedbackTimeout);
                this.session.currentIndex++;
                this.showCurrentWord();
            }
        };
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'mc-option-btn';
            btn.textContent = isEnToJp ? opt.japanese : opt.word;
            btn.disabled = false;
            btn.onclick = () => {
                // すでにフィードバック表示中なら即次へ
                if (this._answered && feedback.textContent) {
                    if (feedbackTimeout) clearTimeout(feedbackTimeout);
                    this.session.currentIndex++;
                    this.showCurrentWord();
                    return;
                }
                if (this._answered) return;
                this._answered = true;
                Array.from(this.elements.mcOptions.children).forEach(b => b.disabled = true);
                const isCorrect = isEnToJp
                    ? (btn.textContent === currentWord.japanese)
                    : (btn.textContent === currentWord.word);
                if (isCorrect) {
                    btn.classList.add('correct');
                    feedback.textContent = '正解！';
                    feedback.style.color = '#4caf50';
                } else {
                    btn.classList.add('incorrect');
                    feedback.textContent = '不正解...';
                    feedback.style.color = '#f44336';
                    // 正解の選択肢にも色を付ける
                    Array.from(this.elements.mcOptions.children).forEach(b => {
                        if ((isEnToJp && b.textContent === currentWord.japanese) || (!isEnToJp && b.textContent === currentWord.word)) {
                            b.classList.add('correct');
                        }
                    });
                }
                // 回答記録
                this.answerLogs.push({
                    word: currentWord.word,
                    japanese: currentWord.japanese,
                    userAnswer: btn.textContent,
                    isCorrect: isCorrect
                });
                if (isCorrect) {
                    this.session.correctCount++;
                } else {
                    this.session.incorrectCount++;
                }
                // 数秒後に自動で次の問題へ
                feedbackTimeout = setTimeout(() => {
                    this.session.currentIndex++;
                    this.showCurrentWord();
                }, 1000);
            };
            this.elements.mcOptions.appendChild(btn);
        });
    }
    showAnswer() {
        this.session.showingAnswer = true;
        this.elements.cardFront.style.display = 'none';
        this.elements.cardBack.style.display = 'block';
    }
    markAnswer(isCorrect, userAnswer) {
        if (this.studyType === 'flashcard' && !this.session.showingAnswer)
            return;
        const currentWord = this.session.words[this.session.currentIndex];
        if (userAnswer === undefined) {
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
        // 履歴保存
        saveStudyHistory({
            date: new Date().toLocaleString(),
            correct: this.session.correctCount,
            incorrect: this.session.incorrectCount,
            accuracy: (this.session.correctCount + this.session.incorrectCount) > 0 ? Math.round((this.session.correctCount / (this.session.correctCount + this.session.incorrectCount)) * 100) : 0,
            total: this.session.correctCount + this.session.incorrectCount,
            wrongWords: this.answerLogs.filter(log => !log.isCorrect).map(log => ({ word: log.word, japanese: log.japanese }))
        });
    }
    setupCsvFileInput() {
        const csvInput = document.getElementById('csvFileInput');
        if (!csvInput) return;
        csvInput.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (event) => {
                const csvText = event.target.result;
                // ファイル名を一意にする
                const fileName = file.name.replace(/[^\w\d\-_\.]/g, '_');
                // 既存リストに追加
                if (!this.availableFiles.includes(fileName)) {
                    this.availableFiles.push(fileName);
                }
                // 仮想ファイルとして内容を保存
                if (!this._virtualFiles) this._virtualFiles = {};
                this._virtualFiles[fileName] = csvText;
                // チェックボックス再描画
                this.initFileCheckboxes();
                // 追加したファイルを選択状態に
                this.selectedFiles = [fileName];
                this.loadWords();
            };
            reader.readAsText(file, 'utf-8');
        });
    }
    startReviewSession(wrongWords) {
        this.session = {
            words: wrongWords,
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
}
const APP_VERSION = 'v0.15.0';
const CHANGELOG = [
    'v0.15.0: UIをシンプルに整理・再設計（ファイル選択・進捗・ボタン配置・余白など）',
    'v0.14.0: 音声読み上げ（英単語の発音）機能を追加',
    'v0.13.0: 学習履歴の自動保存・一覧表示・削除・苦手単語復習機能を追加',
    'v0.12.3: 単語リスト編集ボタンの初期化タイミングを修正し、正常に動作するよう改善',
    'v0.12.2: ユーザーがCSVファイルをアップロードして学習ファイルとして利用できる機能を追加',
    'v0.12.1: 単語リスト編集モーダルのテーブルに縦スクロールを追加し、多数の単語も編集しやすく改善',
    'v0.12.0: 単語リスト編集UI（追加・編集・削除）機能を追加',
    'v0.11.0: 変更履歴を動的に表示するように修正。バージョン情報と変更履歴をフッターに表示。',
    'v0.10.0: 四択モードで正誤フィードバックを毎回表示。不正解時は正解選択肢を強調。単語部分や選択肢再クリックで即次の問題へ進む仕様を追加。',
    'v0.9.0: ファビコンをGoogleのものに変更。UIの細部デザインを調整。',
    'v0.8.0: 四択モード（multiple-choice）を実装。選択肢ランダム化・出題数制限対応。',
    'v0.7.0: 複数CSVファイルの同時選択・出題数指定機能を追加。ファイル選択UIをチェックボックス化。',
    'v0.6.0: 学習完了画面・正誤表（解答一覧）を追加。正解率・正誤数を表示。',
    'v0.5.1: ダークモード切替ボタン追加。テーマ切替時の配色バグ修正。',
    'v0.5.0: フラッシュカード基本機能（英→日/日→英切替、正誤カウント、進捗バー）を実装。',
    'v0.4.0: CSVファイルから単語リストを読み込み、学習セッションを生成する機能を追加。',
    'v0.3.0: UIデザインをモダン化。レスポンシブ対応。',
    'v0.2.0: 単語リストのシャッフル・リスタート機能を追加。',
    'v0.1.0: プロトタイプ作成。英単語・日本語の表示のみ対応。'
];

function updateFooterVersionAndChangelog() {
    const versionInfo = document.getElementById('versionInfo');
    if (versionInfo) versionInfo.textContent = `バージョン: ${APP_VERSION}`;
    const changelog = document.getElementById('changelog');
    if (changelog) {
        let html = '<b>変更履歴</b><ul style="margin:8px 0 0 1.2em;padding:0;text-align:left;">';
        for (const log of CHANGELOG) {
            html += `<li>${log}</li>`;
        }
        html += '</ul>';
        changelog.innerHTML = html;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateFooterVersionAndChangelog();
    const app = new VocabularyApp();
    setupHistoryModal(app);
    // PC判定
    const isPC = window.matchMedia('(pointer:fine)').matches && window.innerWidth > 900;
    if (isPC) {
        const help = document.getElementById('pcHelp');
        if (help) {
            help.style.display = '';
            help.innerHTML = `
                <b>操作方法（PC）</b><br>
                ・スペースキー/Enter：答えを表示<br>
                ・1/→キー：正解<br>
                ・2/←キー：不正解<br>
                ・マウスクリック：各ボタン操作<br>
                ・テーマ切替：右上のボタン<br>
                <span style='font-size:0.95em;color:#888;'>※ 四択モード時は選択肢をクリックしてください</span>
            `;
        }
    }
});

function initWordListEditor() {
    const editBtn = document.getElementById('editWordListBtn');
    const modalBg = document.getElementById('wordListModalBg');
    const closeBtn = document.getElementById('closeWordListModal');
    const tableBody = document.querySelector('#wordListTable tbody');
    const addBtn = document.getElementById('addWordBtn');
    const newWordInput = document.getElementById('newWordInput');
    const newJapaneseInput = document.getElementById('newJapaneseInput');
    let editingIndex = null;
    let wordList = [];
    // CSVファイルから現在の単語リストを取得
    async function loadCurrentWordList() {
        // ここでは最初のファイルを編集対象とする
        const file = 'Grammar_words(前期中間).csv';
        const response = await fetch(file);
        const csvText = await response.text();
        const lines = csvText.trim().split('\n').slice(1);
        wordList = lines.map(line => {
            const [word, japanese] = line.split(',');
            return { word: word ? word.trim() : '', japanese: japanese ? japanese.trim() : '' };
        });
        renderTable();
    }
    function renderTable() {
        tableBody.innerHTML = '';
        wordList.forEach((row, idx) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td><input type='text' value='${row.word}' data-idx='${idx}' class='edit-word'></td><td><input type='text' value='${row.japanese}' data-idx='${idx}' class='edit-japanese'></td><td><button class='edit-btn' data-idx='${idx}'>保存</button><button class='delete-btn' data-idx='${idx}'>削除</button></td>`;
            tableBody.appendChild(tr);
        });
    }
    // 編集・削除イベント
    tableBody.addEventListener('click', e => {
        if (e.target.classList.contains('edit-btn')) {
            const idx = +e.target.dataset.idx;
            const word = tableBody.querySelector(`input.edit-word[data-idx='${idx}']`).value.trim();
            const japanese = tableBody.querySelector(`input.edit-japanese[data-idx='${idx}']`).value.trim();
            wordList[idx] = { word, japanese };
            renderTable();
        } else if (e.target.classList.contains('delete-btn')) {
            const idx = +e.target.dataset.idx;
            wordList.splice(idx, 1);
            renderTable();
        }
    });
    // 追加イベント
    addBtn.addEventListener('click', () => {
        const word = newWordInput.value.trim();
        const japanese = newJapaneseInput.value.trim();
        if (!word || !japanese) return;
        wordList.push({ word, japanese });
        newWordInput.value = '';
        newJapaneseInput.value = '';
        renderTable();
    });
    // モーダル表示・非表示
    editBtn.addEventListener('click', () => {
        modalBg.style.display = 'flex';
        loadCurrentWordList();
    });
    closeBtn.addEventListener('click', () => {
        modalBg.style.display = 'none';
    });
    // モーダル外クリックで閉じる
    modalBg.addEventListener('click', e => {
        if (e.target === modalBg) modalBg.style.display = 'none';
    });
    // 保存（ダウンロード）機能
    // 本来はサーバー保存だが、ここではCSVダウンロードで対応
    const saveBtn = document.createElement('button');
    saveBtn.textContent = 'CSVとして保存';
    saveBtn.className = 'add-row-btn';
    saveBtn.style.marginLeft = '10px';
    saveBtn.onclick = () => {
        let csv = 'word,japanese\n';
        wordList.forEach(row => {
            csv += `${row.word},${row.japanese}\n`;
        });
        const blob = new Blob([csv], { type: 'text/csv' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'Grammar_words(前期中間)_edited.csv';
        a.click();
        URL.revokeObjectURL(url);
    };
    document.querySelector('.modal').appendChild(saveBtn);
}

function saveStudyHistory(entry) {
    const key = 'studyHistory';
    let history = [];
    try { history = JSON.parse(localStorage.getItem(key)) || []; } catch(e) {}
    history.unshift(entry);
    if (history.length > 30) history = history.slice(0, 30);
    localStorage.setItem(key, JSON.stringify(history));
}

function loadStudyHistory() {
    try { return JSON.parse(localStorage.getItem('studyHistory')) || []; } catch(e) { return []; }
}

function deleteStudyHistory(index) {
    let history = loadStudyHistory();
    history.splice(index, 1);
    localStorage.setItem('studyHistory', JSON.stringify(history));
}

function setupHistoryModal(app) {
    const showBtn = document.getElementById('showHistoryBtn');
    const modalBg = document.getElementById('historyModalBg');
    const closeBtn = document.getElementById('closeHistoryModal');
    const listDiv = document.getElementById('historyList');
    function render() {
        const history = loadStudyHistory();
        if (!history.length) {
            listDiv.innerHTML = '<div style="color:#ccc;padding:20px;">履歴がありません</div>';
            return;
        }
        let html = '<table style="width:100%;margin-bottom:10px;"><thead><tr><th>日付</th><th>正解/全体</th><th>正答率</th><th>苦手単語</th><th>操作</th></tr></thead><tbody>';
        history.forEach((h, i) => {
            html += `<tr><td>${h.date}</td><td>${h.correct}/${h.total}</td><td>${h.accuracy}%</td><td>${h.wrongWords.length}</td><td><button class='delete-history-btn' data-idx='${i}'>削除</button> <button class='review-wrong-btn' data-idx='${i}'>復習</button></td></tr>`;
        });
        html += '</tbody></table>';
        html += '<div style="font-size:0.95em;color:#888;">苦手単語数をクリックで詳細表示</div>';
        listDiv.innerHTML = html;
        // 詳細表示
        Array.from(listDiv.querySelectorAll('td:nth-child(4)')).forEach((td, i) => {
            td.style.cursor = 'pointer';
            td.onclick = () => {
                const wrong = history[i].wrongWords;
                if (!wrong.length) { alert('苦手単語はありません'); return; }
                alert(wrong.map(w => `${w.word} : ${w.japanese}`).join('\n'));
            };
        });
        // 削除
        Array.from(listDiv.querySelectorAll('.delete-history-btn')).forEach(btn => {
            btn.onclick = () => { deleteStudyHistory(+btn.dataset.idx); render(); };
        });
        // 復習
        Array.from(listDiv.querySelectorAll('.review-wrong-btn')).forEach(btn => {
            btn.onclick = () => {
                const wrong = history[+btn.dataset.idx].wrongWords;
                if (!wrong.length) { alert('苦手単語はありません'); return; }
                modalBg.style.display = 'none';
                app.startReviewSession(wrong);
            };
        });
    }
    showBtn.addEventListener('click', () => { modalBg.style.display = 'flex'; render(); });
    closeBtn.addEventListener('click', () => { modalBg.style.display = 'none'; });
    modalBg.addEventListener('click', e => { if (e.target === modalBg) modalBg.style.display = 'none'; });
}

function speakEnglish(word) {
    if (!window.speechSynthesis) {
        alert('このブラウザは音声読み上げに対応していません');
        return;
    }
    const utter = new SpeechSynthesisUtterance(word);
    utter.lang = 'en-US';
    utter.rate = 0.95;
    utter.pitch = 1.0;
    window.speechSynthesis.speak(utter);
}
