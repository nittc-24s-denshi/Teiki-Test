<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>一文表示型 穴埋め問題作成アプリ Ver.11</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Base styles are now primarily handled by Tailwind classes in HTML */
        /* Custom scrollbar for dark mode (optional, for webkit browsers) */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background-color: #e2e8f0; /* slate-200 */
        }
        .dark ::-webkit-scrollbar-track {
            background-color: #334155; /* slate-700 */
        }
        ::-webkit-scrollbar-thumb {
            background-color: #94a3b8; /* slate-400 */
            border-radius: 9999px;
        }
        .dark ::-webkit-scrollbar-thumb {
            background-color: #64748b; /* slate-500 */
        }
        ::-webkit-scrollbar-thumb:hover {
            background-color: #64748b; /* slate-500 */
        }
        .dark ::-webkit-scrollbar-thumb:hover {
            background-color: #475569; /* slate-600 */
        }

        .text-display-area {
            white-space: pre-wrap; 
            line-height: 1.85;
        }

        .blank {
            display: inline-block;
            border-bottom-width: 1.5px;
            border-bottom-style: dashed;
            margin: 0 1px;
            padding: 0 1px;
            text-align: center;
            font-weight: 600; /* semibold */
            cursor: pointer;
            transition: background-color 0.2s;
            vertical-align: baseline; 
            white-space: nowrap; 
            overflow: hidden;
        }

        .revealed-in-place {
            display: inline-block;
            border-bottom: 1.5px solid transparent;
            margin: 0 1px;
            padding: 0 1px;
            font-weight: 600; /* semibold */
            border-radius: 3px;
            cursor: default;
            white-space: pre-wrap; 
            vertical-align: baseline;
        }
        .toast-message {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            /* Tailwind classes for styling */
        }
        /* Range slider custom styles */
        input[type="range"] {
            -webkit-appearance: none;
            appearance: none;
            width: 100%;
            height: 8px;
            border-radius: 4px;
            @apply bg-slate-300 dark:bg-slate-600;
            outline: none;
            opacity: 0.7;
            transition: opacity .2s;
        }
        input[type="range"]:hover {
            opacity: 1;
        }
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            @apply bg-sky-500 dark:bg-sky-400;
            cursor: pointer;
            border: 2px solid white; /* Optional: add a border to the thumb */
            @apply dark:border-slate-700;
        }
        input[type="range"]::-moz-range-thumb {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            @apply bg-sky-500 dark:bg-sky-400;
            cursor: pointer;
            border: 2px solid white;
            @apply dark:border-slate-700;
        }
    </style>
    <script>
        // Manage dark mode
        function applyDarkModePreference() {
            if (localStorage.getItem('darkMode') === 'true' || 
                (!('darkMode' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
            updateDarkModeIcon(); 
        }

        function toggleUserDarkMode() {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('darkMode', 'false');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('darkMode', 'true');
            }
            updateDarkModeIcon();
        }
        
        function updateDarkModeIcon() {
            const sunIcon = document.getElementById('sunIcon');
            const moonIcon = document.getElementById('moonIcon');
            if (!sunIcon || !moonIcon) return; 

            if (document.documentElement.classList.contains('dark')) {
                sunIcon.classList.remove('hidden');
                moonIcon.classList.add('hidden');
            } else {
                moonIcon.classList.remove('hidden');
                sunIcon.classList.add('hidden');
            }
        }
        applyDarkModePreference(); 
    </script>
</head>
<body class="bg-slate-100 dark:bg-slate-900 text-slate-800 dark:text-slate-200 transition-colors duration-300 flex flex-col items-center min-h-screen py-6 px-2 sm:py-8 sm:px-4">
    <div class="bg-white dark:bg-slate-800 p-4 sm:p-6 rounded-lg shadow-xl w-full max-w-2xl">
        <header class="mb-6 pb-3 border-b-2 border-sky-200 dark:border-sky-700 flex justify-between items-center">
            <h1 class="text-2xl sm:text-3xl font-bold text-sky-600 dark:text-sky-400">
                穴埋め問題チャレンジ
            </h1>
            <button id="darkModeToggle" aria-label="Toggle dark mode" class="p-2 rounded-full hover:bg-slate-200 dark:hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-sky-500 transition-colors">
                <svg id="sunIcon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-slate-700 dark:text-slate-300 hidden"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                <svg id="moonIcon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-slate-700 dark:text-slate-300 hidden"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
            </button>
        </header>

        <section class="mb-4">
            <div class="text-md sm:text-lg font-semibold text-sky-600 dark:text-sky-400 text-center">
                <span id="sentenceCounter">文 1 / X</span>
            </div>
        </section>

        <section id="quizInteractionArea" class="bg-white dark:bg-slate-800 p-4 sm:p-6 rounded-lg shadow-xl mb-6 border border-slate-200 dark:border-slate-700">
            <h2 class="text-xl sm:text-2xl font-semibold text-slate-700 dark:text-slate-200 mb-3 text-center">穴埋め問題 <span class="text-sm font-normal">(空欄をクリック)</span></h2>
            
            <div id="japaneseHint" class="bg-sky-50 dark:bg-sky-900 border-l-4 border-sky-400 dark:border-sky-600 text-sky-700 dark:text-sky-300 p-3 rounded-md text-base mb-4 shadow-sm">
                </div>

            <div class="mb-4 p-3 bg-slate-50 dark:bg-slate-700 rounded-md shadow-sm">
                <label for="percentageSlider" class="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">穴埋めにする割合: <span id="percentageValue" class="font-bold text-sky-600 dark:text-sky-400">50</span>%</label>
                <input type="range" id="percentageSlider" name="percentageSlider" min="0" max="100" value="50" step="5" class="w-full h-2 bg-slate-200 dark:bg-slate-600 rounded-lg appearance-none cursor-pointer">
            </div>

            <div id="questionArea" class="text-display-area border border-slate-300 dark:border-slate-600 bg-slate-50 dark:bg-slate-700 text-slate-800 dark:text-slate-100 rounded-md p-3 min-h-[100px] sm:min-h-[80px]">
                </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-4">
                <button id="showAnswerButton" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2.5 px-4 rounded-md shadow-md transition-colors focus:outline-none focus:ring-2 focus:ring-blue-400">
                    全ての空欄を表示
                </button>
                <button id="resetCurrentSentenceButton" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2.5 px-4 rounded-md shadow-md transition-colors focus:outline-none focus:ring-2 focus:ring-orange-400">
                    新しい問題 (同じ文)
                </button>
            </div>

            <div class="flex justify-between items-center mt-6 pt-4 border-t border-slate-200 dark:border-slate-700">
                <button id="prevSentenceButton" class="bg-slate-500 hover:bg-slate-600 dark:bg-slate-600 dark:hover:bg-slate-500 text-white font-medium py-2 px-5 rounded-md shadow-sm disabled:opacity-50 disabled:cursor-not-allowed transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400">
                    &larr; 前へ
                </button>
                <button id="nextSentenceButton" class="bg-slate-500 hover:bg-slate-600 dark:bg-slate-600 dark:hover:bg-slate-500 text-white font-medium py-2 px-5 rounded-md shadow-sm disabled:opacity-50 disabled:cursor-not-allowed transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400">
                    次へ &rarr;
                </button>
            </div>
        </section>

        <footer class="mt-6 text-center">
            <button id="restartButton" class="w-full sm:w-auto bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg text-lg transition-colors focus:outline-none focus:ring-2 focus:ring-indigo-400">
                全問やり直し (シャッフル)
            </button>
        </footer>
    </div>

    <script>
        // --- データ定義 ---
        const sentenceData = [
            // Conversation 1
            { english: "A: What kind of sport do you like playing?", japanese: "A: どんなスポーツをするのが好き?" },
            { english: "B: I like playing lacrosse, so I'm on the school lacrosse team.", japanese: "B: ラクロスをするのが好きで、学校のラクロスチームに入っています。" },
            { english: "A: Have you ever heard of lacrosse?", japanese: "A: ラクロスのこと聞いたことある?" },
            { english: "B: Yeah, but I know almost nothing about it.", japanese: "B: ええ、でもほとんど何も知らないわ。" },
            { english: "It's a team sport played with a ball and a long stick with a net, isn't it?", japanese: "ボールとネットのついた長いスティックでプレーするチームスポーツですよね?" },
            { english: "A: Yes. I hear the number of lacrosse players has tripled in the past few years.", japanese: "A: はい。ここ数年でラクロスの選手数が3倍になったと聞いています。" },
            { english: "B: Sounds interesting! How about joining our team?", japanese: "B: 面白そうですね! 私たちのチームに入りませんか?" },
            { english: "A: OK, let me think a bit about it.", japanese: "A: OK、少し考えさせて。" },
            { english: "B: I highly recommend joining the team.", japanese: "B: チームに入ることを強くお勧めします。" },
            { english: "A: Thanks. I'm not sure yet, but I'll come to the practice this Saturday and see how it goes.", japanese: "A: ありがとう。まだわからないけど、今週の土曜日に練習に行って、どんな感じか見てみるよ。" },
            { english: "A: Do you often play against other teams?", japanese: "A: よく他のチームと試合をするの?" },
            { english: "B: Of course. Next month, we will have a big tournament with dozens of teams.", japanese: "B: もちろん。来月、たくさんのチームが出る大きなトーナメントがあるの。" },
            { english: "I think it's worth watching.", japanese: "見る価値があると思うわ。" },
            { english: "A: That sounds great! I'll be there. I'm looking forward to seeing it.", japanese: "A: すごいわね! 見に行くよ。見るのが楽しみだ。" },
            // Conversation 3
            { english: "A: Emily, what are you looking at?", japanese: "A: エミリー、何を見ているの?" },
            { english: "B: A picture of my family. Here. Take a look!", japanese: "B: 家族の写真です。ほら、見てください!" },
            { english: "A: Oh, what a lovely family!", japanese: "A: まあ、なんてすてきな家族なの!" },
            { english: "B: Thanks. The girl wearing a white dress is my sister, and the woman sitting next to her is my mother.", japanese: "B: ありがとう。白いドレスを着ている女の子が私の妹で、その隣に座っている女性が母です。" },
            { english: "A: They said they had it taken just now.", japanese: "A: ちょうど今その写真を撮ったばかりだそうですよ。" },
            { english: "B: Really? That was impossible when I was abroad in college.", japanese: "B: 本当に? 大学留学中はそんなこと不可能だったわ。" },
            { english: "It took days for letters to arrive. We exchange messages and pictures many times a day.", japanese: "手紙が届くのに数日かかったのよ。1日に何回もメッセージや写真のやりとりをしているから、" },
            { english: "So I'm not so homesick.", japanese: "それほどホームシックにはなっていません。" },
            { english: "A: That's good. I really think that digital media has come a long way.", japanese: "A: それはいいね。デジタルメディアは大きく進歩したと本当に思うわ。" },
            // Conversation 4
            { english: "A: Emily, have you got used to living in Japan?", japanese: "A: エミリー、日本での生活に慣れましたか?" },
            { english: "B: Yes.", japanese: "B: はい。" },
            { english: "I sometimes found life here difficult to get used to because there are a lot of differences in lifestyle.", japanese: "生活様式の違いがたくさんあるので、時々ここでの生活に慣れるのは難しいと思いましたが。" },
            { english: "A: From what you said, I am sure you have made good friends.", japanese: "A: 君の言ったことからすると、良い友だちができたんですね。" },
            { english: "B: Of course. My classmates are all friendly.", japanese: "B: もちろんです。クラスメートはみんな親しみやすいです。" },
            { english: "Generally speaking, Japanese like to speak modestly, so people from other countries are often confused.", japanese: "一般的に、日本人は控えめに話すことを好むので、外国人は困惑することがよくあります。" },
            { english: "A: Do you agree?", japanese: "A: 君もそう思いますか。" },
            { english: "B: It is not always so. Most of my friends say what they think quite clearly.", japanese: "B: 必ずしもそうとは思いません。ほとんどの友だちは自分の考えていることをとてもはっきりと言ってくれます。" },
            // Conversation 5
            { english: "A: John, I heard there is no 1 cent coin in Australia.", japanese: "A: ジョン、オーストラリアの通貨には1セント硬貨がないって聞いたんだけど。" },
            { english: "B: That's right.", japanese: "B: そうだよ。" },
            { english: "A: They stopped making them because they are too expensive to make.", japanese: "A: 製造にお金がかかりすぎるから廃止したんだ。" },
            { english: "B: But the prices haven't changed.", japanese: "B: でも値段は変わってないね。" },
            { english: "So, the price tag might say $1.99, but you can't pay what it says on the tag in cash.", japanese: "だから、値段が1.99ドルっていうのもありえるけど、値札どおりには現金で払えないね。" },
            { english: "A: In other words, you often have to pay more.", japanese: "A: 言い換えると、多く払わないといけないことがよくあるってことだね。" },
            { english: "B: Yes, and sometimes you pay less.", japanese: "B: そうだね、少なく払うこともあるよ。" },
            { english: "But the ways in which people pay are changing, too. Nowadays, most people don't pay in cash.", japanese: "でも支払い方も変わってきているよ。近ごろはほとんどの人は現金で払わないんだ。" }
        ];

        // --- DOM要素 ---
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
        let shuffledSentenceIndices = [];
        let currentShuffledIndex = 0;
        let originalWords = [];
        let selectedIndices = new Set();
        let offscreenSpan; 

        // --- 初期化処理 ---
        function shuffleArray(array) {
            const newArray = [...array];
            for (let i = newArray.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
            }
            return newArray;
        }
        
        function initializeApp(isRestart = false) {
            offscreenSpan = document.createElement('span');
            offscreenSpan.style.visibility = 'hidden';
            offscreenSpan.style.position = 'absolute';
            offscreenSpan.style.whiteSpace = 'pre'; 
            document.body.appendChild(offscreenSpan);

            shuffledSentenceIndices = shuffleArray([...Array(sentenceData.length).keys()]);
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
            const actualSentenceIndex = shuffledSentenceIndices[currentShuffledIndex];
            const currentSentence = sentenceData[actualSentenceIndex];

            japaneseHintEl.textContent = currentSentence.japanese;
            japaneseHintEl.classList.remove('hidden'); 
            
            originalWords = currentSentence.english.match(/\b[\w'-]+\b|[^\s\w'-]|[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF々〇〻\u31F0-\u31FF]+|\n/g) || [];
            
            performAutoSelectionAndGenerateQuestion();

            showAnswerButton.textContent = '全ての空欄を表示';
            sentenceCounterEl.textContent = `文 ${currentShuffledIndex + 1} / ${sentenceData.length}`;
            
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
            
           