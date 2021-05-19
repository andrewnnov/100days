import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


lives = 6

word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)

display = []
for _ in range(len(choosen_word)):
    display.append('_')                



#Testing code
print(f'Psss, the solution is {choosen_word}.')
print(display)
print(stages[lives])

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(guess)

    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
        
    if guess not in choosen_word:
            lives = lives - 1
            print("The letter Your choose is not in the word")
            if lives == 0:
                end_of_game = True
                print("You lose")
                
                

    print(display)
    print(stages[lives])
    #print(lives)

    
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    




