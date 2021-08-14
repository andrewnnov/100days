import pandas

# Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

data_dictionary_alf = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter the word: ")
user_word_cap = user_word.upper()

list_of_letter = []
for letter in user_word_cap:
    if letter in data_dictionary_alf.keys():
        list_of_letter.append(data_dictionary_alf[letter])


print(list_of_letter)
