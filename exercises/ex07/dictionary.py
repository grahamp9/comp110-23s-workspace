"""EX07 a dictionary."""
__author__ = "730408563"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values from a dictionary."""
    new_dict: dict[str, str] = {}
    for item in old_dict:
        if old_dict[item] in new_dict:
            raise KeyError("duplicate number detected")
        new_dict[old_dict[item]] = item
    return new_dict


def favorite_color(name_color: dict[str, str]) -> str:
    """Identifies the color that occurs the most frequently or whichever was first if there is a tie."""
    color_count: dict[str, int] = {}
    for color in name_color:
        if name_color[color] not in color_count:
            color_count[name_color[color]] = 1
        else:
            color_count[name_color[color]] += 1
    final_count = 0 
    common_color: str = ""
    for color in color_count:
        if color_count[color] > final_count:
            final_count = color_count[color]
            common_color = color
    return common_color


def count(val: list[str]) -> dict[str, int]:
    """Counts how many times each string appears."""
    store: dict[str, int] = {}
    for item in val:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store
