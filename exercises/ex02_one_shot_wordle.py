"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730408563"

secret_word: str = str("python")
guess: str = str(input(f"What is your {len(secret_word)}-letter guess? "))
guess_indx: int = 0 
emoji_guess = ""
character_search = False
alt_indx = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)}-letters! Try again: ") 
while guess_indx < len(secret_word):
    if secret_word[guess_indx] == guess[guess_indx]:
        emoji_guess = emoji_guess + GREEN_BOX
    else:
        alt_indx = 0
        character_search = False
        while character_search is False and alt_indx < len(secret_word): 
            if secret_word[alt_indx] == guess[guess_indx]:
                character_search = True
            alt_indx = alt_indx + 1
        if character_search is True:
            emoji_guess = emoji_guess + YELLOW_BOX
        else: 
            emoji_guess = emoji_guess + WHITE_BOX
    guess_indx = guess_indx + 1
print(emoji_guess)

if guess == secret_word: 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
