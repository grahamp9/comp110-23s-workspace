"""EX05 test - testing Utils."""
__author__ = "730408563"

from exercises.ex05.utils import only_evens, concat, sub

#empty or 1 item list for edge cases  

def test_empty()-> None:
    assert only_evens([]) == []

def test_one_element () -> None:
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]

#normal expected length lists for use cases

def test_real() -> None:
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

def test_real_1() -> None:
    test_list: list[int] = [1, 2, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]

#empty or 1 item list for edge cases  

def test_empty_concat()-> None:
   test_list: list[int] = []
   test_list_1: list[int] = []
   assert concat(test_list, test_list_1) == []

def test_two_elements_concat () -> None:
   test_list: list[int] = [2]
   test_list_1: list[int] = [1]
   assert concat(test_list, test_list_1) == [2, 1]

#normal expected length lists for use cases

def test_real_concat() -> None:
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [2, 3, 4]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 2, 3, 4]

def test_real_1_concat() -> None:
    test_list_1: list[int] = [1, 2]
    test_list_2: list[int] = [2, 3, 4, 5, 7]
    assert concat(test_list_1, test_list_2) == [1, 2, 2, 3, 4, 5, 7]

#edge cases

def test_empty_sub()-> None:
    assert sub([],(),()) == []

def test_one_element_sub() -> None:
    test_list: list[int] = [2]
    assert sub(test_list, 2, ()) == []

#use cases

def test_real_sub() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(test_list, 2, 6) == [3, 4, 5, 6]

def test_real_1_sub() -> None:
    test_list: list[int] = [1, 2, 3, 4, 6, 7, 8, 11, 13]
    assert sub(test_list, 0, 7) == [1, 2, 3, 4, 6, 7, 8]
