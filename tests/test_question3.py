from answer.question3 import compress_runs


def test_answer_compress_runs():
    text = "aaabccccdde"
    assert compress_runs(text) == "3a1b4c2d1e"


def test_another_compress_runs():
    text = "ABBBCCDAA"
    assert compress_runs(text) == "1A3B2C1D2A"
