"""File to define Fish class"""

class Fish:


    age: int 

    def __init__(self):
        """Creates new Fish object."""
        self.age = 0 
        return None
    

    def one_day(self):
        """Increases the age of the fish."""
        self.age += 1
        return None