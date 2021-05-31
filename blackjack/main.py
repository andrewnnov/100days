import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def dealer_card():
    return random.choice(cards)


for _ in range(2):
    user_cards.append(dealer_card())
    computer_cards.append(dealer_card())


def calculate_score(list_of_cards):
    sum_of_score = sum(list_of_cards)
    if sum_of_score == 21 and len(list_of_cards):
        return 0
    elif 11 in list_of_cards and sum_of_score > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return 12
    else:
        return sum_of_score

is_game_over = False

#while game_is_continue:
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f" You cards: {user_cards}, current score: {user_score}")
print(f" Computer first card: {computer_cards[0]}")


if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
        
        




