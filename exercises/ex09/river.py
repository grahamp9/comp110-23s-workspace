"""File to define River class"""
__author__ = "730408563"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:

    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())


    def check_ages(self):
        """Checks ages of bears and fish."""
        new_bears: list[Bear] = []
        new_fish: list[Fish] = []
        for bear in self.bears:
            if bear.age >= 5:
                new_bears.append(bear)
        self.bears = new_bears
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        return None


    def bears_eating(self):
        """Removes fish when bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Checks hunger in bears."""
        for bear in self.bears:
            if bear.hunger_score < 0:
                self.bears.pop(0)
        return None
        

    def repopulate_fish(self):
        """Creates more fish offspring if population supports."""
        fish_offspring: Fish = (self.fish//2) * 4
        self.fish.append(fish_offspring)
        return None
    

    def repopulate_bears(self):
        """Creates more bear offspring if population supports."""
        bear_offspring: Bear = (self.bears//2)
        self.bears.append(bear_offspring)
        return None
    

    def view_river(self):
        """Shows the river populations and days."""
        print(f"~~~ Day: {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Fish population: {len(self.bears)}")
        return None
            

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            

    def one_river_week(self):
        """Shows one week in the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None
    

    def remove_fish(self, amount: int):
        """Removes fish from the river."""
        i: int = 0
        while i < (amount - 1):
            self.fish.pop[i]
            i += 1
        return None

