from answer.question6 import unique_ordered


def test_unique_ordered_basic() -> None:
    """基本ケース：整数の重複削除"""
    assert unique_ordered([1, 2, 3, 2, 1, 4, 3, 5]) == [1, 2, 3, 4, 5]


def test_unique_ordered_strings() -> None:
    """文字列の重複削除"""
    assert unique_ordered(["apple", "banana", "apple", "cherry", "banana"]) == [
        "apple",
        "banana",
        "cherry",
    ]


def test_unique_ordered_all_same() -> None:
    """すべて同じ要素"""
    assert unique_ordered([1, 1, 1, 1]) == [1]


def test_unique_ordered_empty() -> None:
    """空のリスト"""
    assert unique_ordered([]) == []


def test_unique_ordered_no_duplicates() -> None:
    """重複なし"""
    assert unique_ordered([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_unique_ordered_single_element() -> None:
    """要素が1つ"""
    assert unique_ordered([42]) == [42]


def test_unique_ordered_preserves_order() -> None:
    """順序が保持されることを確認"""
    assert unique_ordered([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [3, 1, 4, 5, 9, 2, 6]


def test_unique_ordered_alternating() -> None:
    """交互に出現するパターン"""
    assert unique_ordered(["a", "b", "a", "b", "a", "b"]) == ["a", "b"]
