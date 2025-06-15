import { problemSets } from './sentenceData.js';

// --- DOM要素 ---
const problemSetListEl = document.getElementById('problemSetList');
const currentSetInfoEl = document.getElementById('currentSetInfo');
const japaneseHintEl = document.getElementById('japaneseHint');
const sentenceCounterEl = document.getElementById('sentenceCounter');
const prevSentenceButton = document.getElementById('prevSentenceButton');
const nextSentenceButton = document.getElementById('nextSentenceButton');
const restartButton = document.getElementById('restartButton');
const darkModeToggleEl = document.getElementById('darkModeToggle'); 

const percentageSlider = document.getElementById('percentageSlider');
const percentageValueEl = document.getElementById('percentageValue');

const quizInteractionArea = document.getElementById('quizInteractionArea');
const questionAreaEl = document.getElementById('questionArea');
const showAnswerButton = document.getElementById('showAnswerButton');
const resetCurrentSentenceButton = document.getElementById('resetCurrentSentenceButton');

// --- アプリケーションの状態 ---
let selectedProblemSets = new Set();
let allSentences = [];
let shuffledSentenceIndices = [];
let currentShuffledIndex = 0;
let originalWords = [];
let selectedIndices = new Set();
let offscreenSpan; 

// --- 初期化処理 ---
function initializeProblemSetSelector() {
    problemSetListEl.innerHTML = '';
    Object.entries(problemSets).forEach(([key, set]) => {
        const button = document.createElement('button');
        button.className = 'problem-set-button bg-white dark:bg-slate-800 p-3 rounded-lg shadow-sm border border-slate-200 dark:border-slate-600 hover:border-sky-400 dark:hover:border-sky-400 transition-colors text-left';
        button.dataset.setKey = key;
        button.innerHTML = `
            <div class="flex items-center justify-between">
                <div class="font-semibold text-slate-800 dark:text-slate-200">${set.title}</div>
                <div class="problem-set-checkbox w-5 h-5 border-2 border-slate-300 dark:border-slate-600 rounded flex items-center justify-center">
                    <svg class="check-icon hidden w-4 h-4 text-sky-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                    </svg>
                </div>
            </div>
            <div class="text-sm text-slate-600 dark:text-slate-400 mt-1">${set.description}</div>
            <div class="text-xs text-slate-500 dark:text-slate-500 mt-1">${set.sentences.length}問</div>
        `;
        button.addEventListener('click', (event) => toggleProblemSet(key, event));
        problemSetListEl.appendChild(button);
    });
}

function toggleProblemSet(setKey, event) {
    const button = event.currentTarget;
    const checkbox = button.querySelector('.problem-set-checkbox');
    const checkIcon = button.querySelector('.check-icon');
    
    if (selectedProblemSets.has(setKey)) {
        selectedProblemSets.delete(setKey);
        button.classList.remove('border-sky-400', 'dark:border-sky-400', 'ring-2', 'ring-sky-400');
        checkbox.classList.remove('bg-sky-50', 'dark:bg-sky-900', 'border-sky-400', 'dark:border-sky-400');
        checkIcon.classList.add('hidden');
    } else {
        selectedProblemSets.add(setKey);
        button.classList.add('border-sky-400', 'dark:border-sky-400', 'ring-2', 'ring-sky-400');
        checkbox.classList.add('bg-sky-50', 'dark:bg-sky-900', 'border-sky-400', 'dark:border-sky-400');
        checkIcon.classList.remove('hidden');
    }
    
    updateCurrentSetInfo();
    if (selectedProblemSets.size > 0) {
        initializeApp(true);
    } else {
        quizInteractionArea.classList.add('hidden');
    }
}

function updateCurrentSetInfo() {
    if (selectedProblemSets.size === 0) {
        currentSetInfoEl.textContent = '問題セットを選択してください';
        return;
    }

    const selectedSets = Array.from(selectedProblemSets).map(key => problemSets[key]);
    const totalQuestions = selectedSets.reduce((sum, set) => sum + set.sentences.length, 0);
    
    let infoText = '';
    if (selectedSets.length === 1) {
        const set = selectedSets[0];
        infoText = `${set.title} - ${set.description} (${set.sentences.length}問)`;
    } else {
        infoText = `${selectedSets.length}個のセットを選択中 (合計${totalQuestions}問)`;
    }
    currentSetInfoEl.textContent = infoText;
}

function shuffleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
}

function initializeApp(isRestart = false) {
    if (selectedProblemSets.size === 0) {
        quizInteractionArea.classList.add('hidden');
        return;
    }

    // 選択された問題セットから全ての文を収集
    allSentences = [];
    Array.from(selectedProblemSets).forEach(setKey => {
        const set = problemSets[setKey];
        allSentences.push(...set.sentences.map(sentence => ({
            ...sentence,
            setKey,
            setTitle: set.title
        })));
    });

    offscreenSpan = document.createElement('span');
    offscreenSpan.style.visibility = 'hidden';
    offscreenSpan.style.position = 'absolute';
    offscreenSpan.style.whiteSpace = 'pre'; 
    document.body.appendChild(offscreenSpan);

    shuffledSentenceIndices = shuffleArray([...Array(allSentences.length).keys()]);
    currentShuffledIndex = 0;
    displayCurrentSentenceAndQuestion();
    updateNavigationButtons();
    if (isRestart) {
         showToast("問題をシャッフルして最初からやり直します。", "success");
    }
}

function getTextWidth(text, fontStyle) {
    if (!offscreenSpan) return 50; 
    offscreenSpan.textContent = text;
    offscreenSpan.style.font = fontStyle;
    let width = offscreenSpan.offsetWidth;
    if (text === "___") width = Math.max(width, 25);
    return width;
}

// --- 表示と問題生成 ---
function displayCurrentSentenceAndQuestion() {
    if (selectedProblemSets.size === 0) return;

    const actualSentenceIndex = shuffledSentenceIndices[currentShuffledIndex];
    const currentSentence = allSentences[actualSentenceIndex];

    japaneseHintEl.textContent = currentSentence.japanese;
    japaneseHintEl.classList.remove('hidden'); 
    
    originalWords = currentSentence.english.match(/\b[\w'-]+\b|[^\s\w'-]|[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF々〇〻\u31F0-\u31FF]+|\n/g) || [];
    
    performAutoSelectionAndGenerateQuestion();

    showAnswerButton.textContent = '全ての空欄を表示';
    sentenceCounterEl.textContent = `文 ${currentShuffledIndex + 1} / ${allSentences.length}`;
    
    quizInteractionArea.classList.remove('hidden');
}

function performAutoSelectionAndGenerateQuestion() {
    questionAreaEl.innerHTML = ""; 
    if (originalWords.length === 0) {
        questionAreaEl.textContent = "問題文がありません。";
        showToast("問題文がありません。", "warning");
        return;
    }

    selectedIndices.clear();
    const selectableIndices = [];
    originalWords.forEach((word, index) => {
        if (word === '\n') return; 
        if (/[a-zA-Z0-9\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/.test(word) && (word.length > 1 || word.toLowerCase() === 'a' || word.toLowerCase() === 'i')) {
            selectableIndices.push(index);
        }
    });

    if (selectableIndices.length === 0) {
        originalWords.forEach(word => {
            if (word === '\n') {
                questionAreaEl.appendChild(document.createElement('br'));
            } else {
                questionAreaEl.appendChild(document.createTextNode(word + ' '));
            }
        });
        showToast("穴埋めにできる単語がなかったため、元の文（問題形式ではない）を表示します。", "warning");
        return;
    }
    
    const currentPercentage = parseInt(percentageSlider.value, 10) / 100;
    let numToSelect = Math.max(1, Math.floor(selectableIndices.length * currentPercentage));
    if (currentPercentage === 0) numToSelect = 0; // Allow 0% selection
    if (currentPercentage === 1) numToSelect = selectableIndices.length; // Ensure 100% selects all

    numToSelect = Math.min(numToSelect, selectableIndices.length);
    const shuffledSelectable = shuffleArray(selectableIndices);
    for (let i = 0; i < numToSelect; i++) {
        selectedIndices.add(shuffledSelectable[i]);
    }

    if (numToSelect > 0 && selectedIndices.size === 0 && selectableIndices.length > 0) {
         selectedIndices.add(shuffledSelectable[0]);
    }

    if (numToSelect > 0 && selectedIndices.size === 0) {
        questionAreaEl.textContent = "問題の作成に失敗しました。";
         showToast("問題の作成に失敗しました。", "error");
        return;
    }
    generateQuestion();
}

function generateQuestion() {
    questionAreaEl.innerHTML = '';
    const questionAreaStyle = getComputedStyle(questionAreaEl);
    const font = `${questionAreaStyle.fontWeight} ${questionAreaStyle.fontSize}/${questionAreaStyle.lineHeight} ${questionAreaStyle.fontFamily}`;

    originalWords.forEach((word, index) => {
        const originalWordText = word;

        if (originalWordText === '\n') {
            questionAreaEl.appendChild(document.createElement('br'));
            return; 
        }

        if (selectedIndices.has(index)) {
            const blankSpan = document.createElement('span');
            blankSpan.classList.add('blank', 'border-blue-500', 'dark:border-blue-400', 'text-blue-600', 'dark:text-blue-400');
            blankSpan.dataset.originalWord = originalWordText;
            blankSpan.dataset.revealed = 'false';
            
            const tempRevealed = document.createElement('span');
            tempRevealed.classList.add('revealed-in-place', 'text-amber-500', 'dark:text-amber-400', 'bg-amber-50', 'dark:bg-amber-900');
            offscreenSpan.appendChild(tempRevealed);
            const revealedStyle = getComputedStyle(tempRevealed);
            const revealedFont = `${revealedStyle.fontWeight} ${revealedStyle.fontSize}/${revealedStyle.lineHeight} ${revealedStyle.fontFamily}`;
            offscreenSpan.removeChild(tempRevealed);

            const wordWidth = getTextWidth(originalWordText, revealedFont);
            
            blankSpan.style.width = `${wordWidth}px`; 
            blankSpan.style.minWidth = `${wordWidth}px`; 
            blankSpan.textContent = `___`; 
            
            blankSpan.addEventListener('click', function(event) {
                event.stopPropagation(); 
                if (this.dataset.revealed === 'false') {
                    this.textContent = this.dataset.originalWord;
                    this.className = ''; 
                    this.classList.add('revealed-in-place', 'text-amber-500', 'dark:text-amber-400', 'bg-amber-50', 'dark:bg-amber-900');
                    this.dataset.revealed = 'true';
                }
            });
            questionAreaEl.appendChild(blankSpan);
        } else {
            questionAreaEl.appendChild(document.createTextNode(originalWordText));
        }

        if (index < originalWords.length - 1 && originalWords[index+1] !== '\n' && originalWordText !== '\n') {
            questionAreaEl.appendChild(document.createTextNode(' '));
        }
    });
}

function isPunctuation(char) {
    if (char === undefined || char === null) return false;
    return /^[.,;:!?]$/.test(char.trim());
}

function updateNavigationButtons() {
    prevSentenceButton.disabled = currentShuffledIndex === 0;
    nextSentenceButton.disabled = currentShuffledIndex === allSentences.length - 1;
}

function showToast(message, type = 'success') {
    document.querySelectorAll('.toast-message').forEach(toast => toast.remove());
    const toast = document.createElement('div');
    toast.textContent = message;
    toast.className = `toast-message fixed bottom-5 left-1/2 -translate-x-1/2 text-white py-2 px-4 rounded-md shadow-lg text-sm z-50`;
    if (type === 'success') toast.classList.add('bg-emerald-500');
    else if (type === 'error') toast.classList.add('bg-red-500');
    else if (type === 'warning') toast.classList.add('bg-amber-500');
    
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// --- イベントリスナー ---
darkModeToggleEl.addEventListener('click', () => {
    toggleUserDarkMode(); 
});

percentageSlider.addEventListener('input', (event) => {
    percentageValueEl.textContent = event.target.value;
});

percentageSlider.addEventListener('change', (event) => {
    performAutoSelectionAndGenerateQuestion();
    showToast(`穴埋め割合を ${event.target.value}% に変更しました。`, "success");
});

prevSentenceButton.addEventListener('click', () => {
    if (currentShuffledIndex > 0) {
        currentShuffledIndex--;
        displayCurrentSentenceAndQuestion();
        updateNavigationButtons();
    }
});

nextSentenceButton.addEventListener('click', () => {
    if (currentShuffledIndex < allSentences.length - 1) {
        currentShuffledIndex++;
        displayCurrentSentenceAndQuestion();
        updateNavigationButtons();
    } else {
        showToast("全問終了しました！「最初からやり直す」で再度挑戦できます。", "success");
    }
});

restartButton.addEventListener('click', () => {
    initializeApp(true);
});

showAnswerButton.addEventListener('click', () => {
    let allRevealed = true;
    questionAreaEl.querySelectorAll('.blank[data-revealed="false"]').forEach(blank => {
        allRevealed = false; 
        blank.textContent = blank.dataset.originalWord;
        blank.className = ''; 
        blank.classList.add('revealed-in-place', 'text-amber-500', 'dark:text-amber-400', 'bg-amber-50', 'dark:bg-amber-900');
        blank.dataset.revealed = 'true';
    });

    if (allRevealed) {
        showToast("全ての空欄は既に表示されています。", "warning");
    } else {
         showToast("全ての空欄を表示しました。", "success");
    }
});

resetCurrentSentenceButton.addEventListener('click', () => {
    displayCurrentSentenceAndQuestion(); 
    showToast("同じ文で新しい問題を作成しました。", "success");
});

document.addEventListener('DOMContentLoaded', () => {
    initializeProblemSetSelector();
});

window.addEventListener('beforeunload', () => {
    if (offscreenSpan && offscreenSpan.parentNode) {
        offscreenSpan.parentNode.removeChild(offscreenSpan);
    }
}); 