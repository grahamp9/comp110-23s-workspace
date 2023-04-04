"""EX07 a dictionary - test."""
__author__ = "730408563"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_empty_invert() -> None:
    """Tests invert with an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_error_invert() -> None:
    """Tests the when invert reaches a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_real_invert() -> None:
    """Tests a normal dictionary with strings as inputs."""
    test_dict: dict[str, str] = {"Graham": "Phillips", "John": "Long", "Jesse": "Young"}
    assert invert(test_dict) == {"Phillips": "Graham", "Long": "John", "Young": "Jesse"} 


def test_empty_favorite_color() -> None:
    """Tests favorite_color with an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_real_favorite_color() -> None: 
    """Tests favorite_color with a normal dictionary."""
    test_dict: dict[str, str] = {"Graham": "yellow", "John": "blue", "Jesse": "blue", "Paul": "green"}
    assert favorite_color(test_dict) == "blue"


def test_real_favorite_color_1() -> None: 
    """Tests favorite_color with a tie for most favorite."""
    test_dict: dict[str, str] = {"Graham": "yellow", "John": "blue", "Jesse": "blue", "Paul": "yellow"}
    assert favorite_color(test_dict) == "yellow"


def test_empty_count() -> None:
    """Tests count with an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_real_count() -> None:
    """Tests count with a normal list."""
    test_list: list[str] = ["graham", "john", "jesse", "jesse", "graham"]
    assert count(test_list) == {"graham": 2, "john": 1, "jesse": 2}


def test_real_count_1() -> None:
    """Tests count with a longer normal list."""
    test_list: list[str] = ["graham", "john", "jesse", "jesse", "graham", "paul", "karen", "graham", "graham"]
    assert count(test_list) == {"graham": 4, "john": 1, "jesse": 2, "paul": 1, "karen": 1}