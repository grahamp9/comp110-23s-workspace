"""EX03 - a more complete Wordle."""
__author__ = "730408563"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(main_word: str, sgl_letter: str) -> bool: 
    """Searches main word for the given letter"""
    search_indx: int = 0 
    assert len(sgl_letter) == 1 
    while search_indx < len(main_word):
        if main_word[search_indx] == sgl_letter:
            return True
        else:
            search_indx =  search_indx + 1
    return False
       
def emojified(guess_word: str, secret_word: str) -> str:
    """Tests each character and assigns their emoji boxes"""
    assert len(guess_word) == len(secret_word)
    guess_idx: int = 0
    emoji_guess: str = ""
    while guess_idx < len(secret_word):
        if secret_word[guess_idx] == guess_word[guess_idx]:
            emoji_guess = emoji_guess + GREEN_BOX
        elif contains_char(secret_word, guess_word[guess_idx]):
            emoji_guess = emoji_guess + YELLOW_BOX
        else:
            emoji_guess = emoji_guess + WHITE_BOX
        guess_idx = guess_idx + 1
    return emoji_guess

def input_guess(guess_len: int) -> str:
    """Sees if guess length and secret length match"""
    guess: str = str(input(f"Enter a {guess_len} character word: "))
    while guess_len != len(guess):
        guess = input(f"That wasn't {guess_len} chars! Try again: ") 
    return guess

def main() -> None: 
    """The entryoint of the program and main game loop. """
    turn_num: int = 1
    game_won: bool = False 
    secret_word: str =  "codes"
    main_num: int = 7 
    while turn_num < main_num and game_won == False:
        print(f"=== Turn {turn_num}/{main_num - 1} ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            game_won = True
            print(f"You won in {turn_num}/{main_num - 1} turns!")
        else:
            turn_num = turn_num + 1 
    if turn_num >= main_num and game_won == False:
        print(f"X/{main_num - 1} - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()