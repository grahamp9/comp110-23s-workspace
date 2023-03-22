def zip(list_1: list[str],list_2: list[int]) -> dict[str, int]:
    """Makes 1st list keys and 2nd list values."""
    if len(list_1) != len(list_2):
        return dict()
    if len(list_1) == 0 or len(list_2) == 0:
        return dict()
    result: dict[str,int] = {}
    index: int = 0
    for item in list_1:
        result[item] = list_2[index]
        index += 1
    return result 

print(zip(["a", "b", "c"], [1, 2, 3]))