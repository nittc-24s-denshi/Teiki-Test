# パイプライン通しサンプル（仮）

<!-- 仮・イーハトーブ -->

宮沢賢治『注文の多い料理店』（パブリックドメイン）由来の設問と、自作の簡単な数式だけの **仮** データ。教材ではない。

## 再生成

```bash
cd tools
python3 -m pip install -r requirements.txt
python3 run_sample_pipeline.py
```

生成物:

- `RAW/sample_ihatov.pdf`
- `pipeline/`（ページ分割・画像・文字起こし・部分 JSON）
- `structured/questions.json`
- `app_data/`
- あわせて `Web_App/Question_Bank/data/` も更新
