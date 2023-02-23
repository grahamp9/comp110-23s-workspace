"""class practice"""

my_word: str = str(input ("what is your word? "))
word_idx: int = int(input("what is your index? "))

def mimic (my_word: str, idx: int) -> str:
    """Given the string my_words, outputs the same string"""
    return (my_word[word_idx])