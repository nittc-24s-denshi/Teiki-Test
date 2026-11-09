from teiki_pipeline.normalize import normalize_stem, stems_similar


def test_normalize_stem_strips_space_and_punct():
    assert normalize_stem("ガウスの法則！") == normalize_stem("ガウス の 法則")


def test_stems_similar_contains():
    a = "イーハトーブの夢の跡について述べよ"
    b = "仮：イーハトーブの夢の跡について述べよ。"
    assert stems_similar(a, b)
