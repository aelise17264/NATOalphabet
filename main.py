import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet_data)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}
# print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
user_dict = list(user_word)
# print(user_dict)
answer = [alphabet_dict[letter] for letter in user_dict]
print(answer)