import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_words_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_words_dict)

user_word = input("Enter a word you want to convert to NATO phonetic: ").upper()
result = [nato_words_dict[letter] for letter in user_word]
print(result)
