from answer.question4 import sliding_window_max


def test_sliding_window_max_basic():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    assert sliding_window_max(nums, k) == [3, 3, 5, 5, 6, 7]


def test_sliding_window_max_k_is_one():
    nums = [9, 8, 7, 6]
    k = 1

    assert sliding_window_max(nums, k) == [9, 8, 7, 6]
