"""EX04 - 'list' Utility Functions"""
__author__ = "730408563"

def all(int_list: list[int], main_int: int) -> bool:
    """Checks to see if input matches all other numbers"""
    search_idx: int = 0
    while search_idx < len(int_list):
        if int_list[search_idx] != main_int:
            return False
        search_idx = search_idx + 1
    return True
def max(input: list[int]) -> int:
    """Finds the largest interval from a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    search_idx: int = 0
    max_num: int = input[0]
    while search_idx < len(input):
        if input[search_idx] > max_num:
            max_num = input[search_idx]
        search_idx += 1
    return max_num

def is_equal(int_list_2: list[int], int_list_3: list[int]) -> bool:
    """Checks to see if every element at every index is equal"""
    search_idx: int = 0
    if len(int_list_2) != len(int_list_3):
        return False
    while search_idx < len(int_list_2):
        if int_list_2[search_idx] == int_list_3[search_idx]:
            search_idx += 1
        else:
            return False
    return True 
