import pandas

# Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

data_dictionary_alf = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_word = input("Enter a word: ")
    user_word_cap = user_word.upper()

    try:
        list_of_letter = [data_dictionary_alf[letter] for letter in user_word_cap]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(list_of_letter)


generate_phonetic()