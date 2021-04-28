import random
#Step1
word_list = ["ardvark", "baboon", "camel"]

#TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word

choosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(choosen_word)
#random.choice(word_list) - choose from list

#TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess lowercase.

guess = input("Guess a letter: ").lower()
print(guess)

#TODO-3 Check if the letter the user guessed(guess) is one of letters tn the chosen_word

for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


