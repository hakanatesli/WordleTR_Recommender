from wordle import Wordle
from colorama import Fore
import pandas as pd

def main():
    
    word_dataset = load_word_dataset("data/wordle_tr_word.txt")

    wordle = Wordle(word_dataset)

    while wordle.can_attempt: 
        guess = input("Type your guess: ")
        color = input("Type color: ")

        if len(guess) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} characters long.")
            continue
        if len(color) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} characters long.")
            continue
        wordle.attempt(guess,color)
        display_result(wordle)
        wordle.recommend(guess,color)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")

def display_result(wordle: Wordle):
    """
    
    """
    for word,color in zip(wordle.attempts,wordle.colors):
        colored_result_str = convert_result_with_color(word, color)
        print(colored_result_str)
    
    for _ in range(wordle.remaining_attempts):
        print("_ " * wordle.WORD_LENGTH)


def load_word_dataset(path: str):
    """
    
    """
    word_set = set()

    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip()
            word_set.add(word)

    return pd.DataFrame(word_set,columns=['words'])


def convert_result_with_color(word:str, color:str):
    """
    
    """
    result_with_color = []

    for i in range(5):
        character = word[i]
        clr = color[i]

        if clr == 'G':
            color = Fore.GREEN
        elif clr == 'Y':
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        
        colored_letter = color + character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)


if __name__ == "__main__":
    main()
