import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


list_options = [rock, paper, scissors]

y_choose = int(input("Enter your choose: rock(0) or paper(1) or scissors(2): "))

if y_choose >= 0 and y_choose <= 2:
    print(list_options[y_choose])

    computer_choose = random.randint(0, len(list_options)-1)
    print(list_options[computer_choose])

    if y_choose != computer_choose:
        if y_choose == 0 and computer_choose == 2:
            print("You win")
        elif y_choose == 1 and computer_choose == 0:
            print("You win")
        elif y_choose == 2 and computer_choose == 1:
            print("You win")    
        else:
            print("You lose")
    else:
        print("Please try again")
    
else:
    print("You lose")



    








