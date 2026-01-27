from answer.question5 import is_balanced


def test_is_balanced_basic() -> None:
    """基本ケース：括弧が正しく対応している"""
    assert is_balanced("print(data[0])") is True


def test_is_balanced_nested() -> None:
    """ネストされた括弧"""
    assert is_balanced("{a: [1, 2, (3 + 4)]}") is True


def test_is_balanced_wrong_order() -> None:
    """括弧の対応順序が不正"""
    assert is_balanced("([)]") is False


def test_is_balanced_unclosed() -> None:
    """閉じ括弧が足りない"""
    assert is_balanced("(((") is False


def test_is_balanced_extra_close() -> None:
    """閉じ括弧が多い"""
    assert is_balanced("())") is False


def test_is_balanced_empty() -> None:
    """空文字列"""
    assert is_balanced("") is True


def test_is_balanced_no_brackets() -> None:
    """括弧を含まない文字列"""
    assert is_balanced("hello world") is True


def test_is_balanced_single_type() -> None:
    """1種類の括弧のみ"""
    assert is_balanced("((()))") is True
    assert is_balanced("[[[]]]") is True
    assert is_balanced("{{{}}}") is True


def test_is_balanced_mismatch_type() -> None:
    """括弧の種類が一致しない"""
    assert is_balanced("(]") is False
    assert is_balanced("[}") is False
    assert is_balanced("{)") is False
