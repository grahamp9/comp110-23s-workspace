"""EX06 - An Adventure."""
__author__ = "730408563"

from random import randint
points: int = 0
player: str = ""
dragon: str = "\U0001F432"
coin: str = "\U0001FA99"
skull: str = "\U0001F480"


def greet () -> None: 
    """Greets the player."""
    global player 
    player = input("Greetings noble adventurer! What is your name? ")
    
def main() -> None:
    global points
    greet()
    choice_1 = input(f"Hello {player}! Choose one of these options: fight, flip, or flee: ")
    while choice_1 == "flip" or choice_1 == "fight":
        if choice_1 == "flip":
            coin_round ()
            choice_1 = input(f"Hello {player}! Choose one of these options: fight, flip, or flee: ")
        if choice_1 == "fight":
            points = dragon_round(points)
            choice_1 = input(f"Hello {player}! Choose one of these options: fight, flip, or flee: ")
    exit_statement ()
    points = 0

def coin_round () -> None:
    flip_value: int = randint(1,2)
    coin_guess: str = input(f"{coin} Pick heads or tails, {player} {coin} :")
    guess_value: int = ()
    if coin_guess == "heads":
        guess_value = 1 
    elif coin_guess == "tails":
        guess_value = 2 
    else:
        print(f"You loose. Please check your spelling, {player}. Make sure to say 'heads' or 'tails' next time. ")
        exit_statement()
    if guess_value == flip_value:
        print("Correct! You will now choose again....")
        global points
        points += 1
        print (f"points: {points}")
    else:
        print(f"{skull} Sorry, {player}, you guessed incorrectly. {skull}")
        exit_statement ()
        points = 0 

def dragon_round (points: int) -> int:
    dragon_move: str = input(f"{dragon} You encounter a dragon, should you move left, right, up, or down? {dragon}")
    if dragon_move == "down":
        print ("Very nice, you will now choose again.....")
        points += 5
        print (f"points: {points}")
    else:
        exit_statement ()
        points = 0 
    return points


def exit_statement () -> None:
    print(f"{skull} Thank you for playing {player}, good luck in your future adventures! {skull} Points = {points}") 
  
if __name__ == "__main__":
    main()


