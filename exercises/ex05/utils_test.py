"""EX05 test - testing Utils."""
__author__ = "730408563"

from exercises.ex05.utils import only_evens, concat, sub


def test_empty() -> None:
    """Tests only_evens with an empty list."""
    assert only_evens([]) == []


def test_one_element() -> None:
    """Tests when one item is in only_evens."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


def test_real() -> None:
    """Normal test from 3 value list."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_real_1() -> None:
    """Normal test from 5 value list."""
    test_list: list[int] = [1, 2, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_empty_concat() -> None:
    """Tests concat with empty lists."""
    test_list: list[int] = []
    test_list_1: list[int] = []
    assert concat(test_list, test_list_1) == []


def test_two_elements_concat() -> None:
    """Tests when one item is in each list in concat."""
    test_list: list[int] = [2]
    test_list_1: list[int] = [1]
    assert concat(test_list, test_list_1) == [2, 1]


def test_real_concat() -> None:
    """Normal test from two 3 value lists."""
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [2, 3, 4]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 2, 3, 4]


def test_real_1_concat() -> None:
    """Normal test from two lists with different lengths."""
    test_list_1: list[int] = [1, 2]
    test_list_2: list[int] = [2, 3, 4, 5, 7]
    assert concat(test_list_1, test_list_2) == [1, 2, 2, 3, 4, 5, 7]


def test_empty_sub() -> None:
    """Tests sub with an empty list and indexes."""
    assert sub([], (), ()) == []


def test_one_element_sub() -> None:
    """Tests when one item is in sub and end index is empty."""
    test_list: list[int] = [2]
    assert sub(test_list, 2, ()) == []


def test_real_sub() -> None:
    """Normal test with a list that has a length of 7."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(test_list, 2, 6) == [3, 4, 5, 6]


def test_real_1_sub() -> None:
    """Normal test that has a list with some larger values."""
    test_list: list[int] = [1, 2, 3, 4, 6, 7, 8, 11, 13]
    assert sub(test_list, 0, 7) == [1, 2, 3, 4, 6, 7, 8]
