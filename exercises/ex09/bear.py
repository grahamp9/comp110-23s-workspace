"""File to define Bear class."""


class Bear:
    """Creates the Bear class."""

    age: int 
    hunger_score: int 
    
    def __init__(self):
        """Creates a new bear object."""
        self.age = 0
        self.hunger_score = 0 
        return None
    
    def one_day(self):
        """Shows one day for the bear age and hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int): 
        """Shows when a bear eats a fish."""
        self.hunger_score += num_fish
        return None