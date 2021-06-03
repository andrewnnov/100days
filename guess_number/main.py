import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")


def play_game():
    guess_number = random.randint(1, 100)
    print(guess_number)
    result_of_guess = True

    while result_of_guess:
        attempts = 0
        print("I'm thinking of number between 1 and 100")
        level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
        if level == 'hard':
            attempts = 5
            print(f"You have {attempts} attempts to guess the number. ")
        else:
            attempts = 10
            print(f"You have {attempts} attempts to guess the number. ")

        # user_guess = int(input("Make a guess: "))
        while attempts > 0:
            user_guess = int(input("Make a guess: "))
            if user_guess > guess_number:
                attempts = attempts - 1
                print("Less")
                if attempts == 0:
                    print("You lose")
                    result_of_guess = False
            elif user_guess < guess_number:
                print("More")
                attempts = attempts - 1
            else:
                print("You guess")
                play_again = input("Do you want to play again? y - yes, n - no")
                if play_again == "y":
                    play_game()
                else:
                    result_of_guess = False


play_game()