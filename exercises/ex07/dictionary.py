"""EX07 a dictionary"""
__author__ = "730408563"

def invert(old_dict:dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values from a dictionary."""
    new_dict: dict [str, str] = {}
    for item in old_dict:
        if old_dict[item] in new_dict:
            raise KeyError("duplicate number detected")
        new_dict[old_dict[item]] = item
    print(new_dict)
    return new_dict


def favorite_color(name_color: dict[str,str]) -> str:
    """Identifies the color that occurs the most frequently."""
    color_count: dict[str, int] = {}
    for color in name_color:
        if name_color[color] not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

    final_count = 0 
    common_color = None
    for color in name_color:
        if color_count[color] > final_count or (color_count[color] == final_count and color in color_count):
            final_count = color_count[color]
            common_color = color_count[color]
    return common_color


def count(val: list[str]) -> dict[str, int]:
    store: dict[str, int] = {}
    for item in val:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store
