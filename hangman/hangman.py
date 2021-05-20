import random
import hangman_words as dic
import hangman_art as art

lives = 6
choosen_word = random.choice(dic.word_list)

display = []
for _ in range(len(choosen_word)):
    display.append('_')             

print(art.logo)
print("The word is...")

print(display)
print(art.stages[lives])

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()    
    print(guess)

    if guess in display:
        print(f"You've already gussed {guess}")


    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
        
    if guess not in choosen_word:
            lives = lives - 1
            print(f"The letter {guess} Your choose is not in the word. You loose the life.")
            if lives == 0:
                end_of_game = True
                print("You lose")
                print(f"The word was {choosen_word}")
                

    print(display)
    print(art.stages[lives])
    

    
    if "_" not in display:
        end_of_game = True
        print("You win")
        print(f"The word is {choosen_word}")
    
    




