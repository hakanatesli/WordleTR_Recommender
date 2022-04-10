import pandas as pd

class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self,word_dataset: pd.DataFrame):
        self.recommend_dataset = word_dataset
        self.attempts = []
        self.colors = []
        pass

    def attempt(self, word:str, color: str):
        """
        
        """
        word = word.upper()
        color = color.upper()
        self.attempts.append(word)
        self.colors.append(color)
    

    def recommend(self,word: str, color: str):
        """
        
        """
        df = self.recommend_dataset.copy()
        for i in range(5):
            letter = word[i]
            clr = color[i]
            
            if clr == 'G':
                df = df[df['words'].str.get(i) == letter]
            elif clr == 'Y':
                df = df[(df['words'].str.count(letter) > 0) & (df['words'].str.get(i) != letter)]
            elif clr == 'B' and word.count(letter) == 1:
                df = df[df['words'].str.count(letter) == 0]
            elif clr == 'B' and word.count(letter) > 1:
                df = df[df['words'].str.get(i) != letter]
        
        self.recommend_dataset = df

        print(f"Recommend word count : {len(self.recommend_dataset)} \n")
        show = input("Type 1 to see recommends. ")
        if show == "1":
            print(list(self.recommend_dataset['words']))
        

    @property
    def is_solved(self) -> bool:
        return len(self.colors) > 0 and self.colors[-1] == "GGGGG"

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    @property
    def can_attempt(self) -> bool:
        return self.remaining_attempts > 0 and not self.is_solved
        