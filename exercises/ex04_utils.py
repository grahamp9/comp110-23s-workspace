"""EX04 - 'list' Utility Functions"""
__author__ = "730408563"

int_list: list[int] = list()
main_int: int

def all(int_list, main_int) -> bool:
    """Checks to see if input matches all other numbers"""
    search_idx: int = 0
    while search_idx < len(int_list):
        if int_list[search_idx] == main_int:
            search_idx = search_idx + 1
        else:
            return False

def max(input: list[int]) -> int:
    """Finds the largest interval from a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")

def is_equal(int_list_2, int_list_3) -> bool:
    """Checks to see if every element at every index is equal"""
    if int_list_2 == int_list_3:
        return True
    else:
        return False