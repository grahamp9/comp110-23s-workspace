"""EX05 - Utils."""
__author__ = "730408563"

def only_evens(int_list: list[int]) -> list[int]: 
    """Finds the even numbers from a list."""
    even_list: list[int] = list()
    for item in range (0,len(int_list)):
        if int_list[item] % 2 == 0:
            even_list.append(int_list[item])
    return even_list

def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    concat_list: list[int] = list()
    for item in list_1:
        concat_list.append(item)
    for item in list_2:
        concat_list.append(item)
    return concat_list

        
def sub(a_list: list[int], start_idx: int, end_idx: int) -> list [int]:
    if len(a_list) == 0 or start_idx >= len(a_list) or end_idx <= 0:
        return list()
    if end_idx >= len(a_list):
        end_idx = len(a_list) 
    if start_idx < 0:
        start_idx = 0  
    new_list: list[int] = list()
    for item in range(start_idx, end_idx):
        new_list.append(a_list[item])
    return new_list
