import random
#Step1
word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)

display = []
for _ in range(len(choosen_word)):
    display.append('_')                



#Testing code
print(f'Psss, the solution is {choosen_word}.')
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(guess)

    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    




