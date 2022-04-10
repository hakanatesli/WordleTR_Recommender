import pandas as pd

def main():
    input_file_path = "turkce-kelime-database/"
    output_file_path = "wordle_tr_word.txt"

    words = pd.DataFrame(data=None)

    letters = ['A','B','C','Ç','D','E','F','G','H','I','İ','J','K','L',
               'M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z']
    
    for letter in letters:
        txt_path = input_file_path + letter + ".txt"
        df = pd.read_table(txt_path,delimiter="\n",header=None)
        words = words.append(df)
    
    words.columns = ['words']
    five_letter_words = words[words['words'].str.len() == 5].reset_index(drop=True)
    five_letter_words = five_letter_words[five_letter_words['words'].str.find(' ') == -1]
    five_letter_words['words'] = five_letter_words['words'].str.upper()

    
    with open(output_file_path, "w") as f:
        for word in five_letter_words['words']:
            f.write(word + "\n")

    print(f"Number of 5-letter words found: {len(five_letter_words)}")

if __name__ == "__main__":
    main()