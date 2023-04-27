"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730408563"


class Simpy:
    """Create the Simpy Class."""

    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, input: list[float]):
        """Initialize the Simpy class."""
        self.values: list[float] = input

    def __str__(self) -> str:
        """Convert the values into a string."""
        return str(f"Simpy({self.values})")
    
    def fill(self, fill_num: float, add_value: int) -> None:
        """Fill a Simpy with a number."""
        new_list: list[float] = []
        i: int = 0
        while i < add_value:
            new_list.append(fill_num)
            i += 1
        self.values = new_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a range of floats."""
        assert step != 0.0
        new_list: list[float] = []
        add_num: float = start
        while add_num > stop:
            new_list.append(add_num)
            add_num += step
        while add_num < stop:
            new_list.append(add_num)
            add_num += step
        self.values = new_list
    
    def sum(self) -> float:
        """Get the sum of a list of floats."""
        copy_list: list[float] = self.values
        final_num: float = sum(copy_list)
        return final_num

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add a Simpy with another Simpy or a float."""
        new_item: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                new_item.append(self.values[item] + rhs.values[item])
        if isinstance(rhs, float):
            for item in self.values:
                new_item.append(item + rhs)
        return Simpy(new_item)
        
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raise a Simpy by another Simpy or a float."""
        new_item: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                new_item.append(self.values[item] ** rhs.values[item])
        else: 
            for item in self.values:
                new_item.append(item ** rhs) 
        return Simpy(new_item)
        
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Check if the value of a Simpy is equal to another Simpy or set float."""
        new_item: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                if self.values[item] == rhs.values[item]:
                    new_item.append(True)
                else:
                    new_item.append(False)
        else:
            for item in self.values:
                if item == rhs:
                    new_item.append(True)
                else:
                    new_item.append(False)
        return new_item
        
    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Check if a Simpy is greater than a Simpy or set of floats."""
        new_item: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                if self.values[item] > rhs.values[item]:
                    new_item.append(True)
                else:
                    new_item.append(False)
        else:
            for item in range(len(self.values)):
                if self.values[item] > rhs:
                    new_item.append(True)
                else:
                    new_item.append(False)
        return new_item

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Get an item from a Simpy at a given index."""
        if isinstance(rhs, list):
            assert len(self.values) == len(rhs)
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            bool_list: list[bool] = []
            float_list: list[float] = []
            for item in range(len(self.values)):
                if rhs[item] is True:
                    bool_list.append(True)
                if rhs[item] is False:
                    bool_list.append(False)
            i: int = 0
            for item in bool_list:
                if item is True:
                    float_list.append(self.values[i])
                i += 1
            return Simpy(float_list)