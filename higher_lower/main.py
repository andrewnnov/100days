from art import logo
from art import vs
from game_data import data
import random

print(logo)


def compare_followers(first, second):
    if first.get("follower_count") > second.get('follower_count'):
        return 1
    else:
        return 0


total_score: int = 0
game_continue = True

first = data[random.randint(0, len(data) - 1)]

while game_continue:
    second = data[random.randint(0, len(data) - 1)]
    while second == first:
        second = data[random.randint(0, len(data) - 1)]

    print(f"Compare A: {first.get('name')}, {first.get('description')}, {first.get('country')}")
    print(vs)
    print(f"Compare B: {second.get('name')}, {second.get('description')}, {second.get('country')}")

    user_choose = input("Who has more followers? Type 'A' or 'B': ")

    if user_choose == 'A':
        if compare_followers(first, second) == 1:
            total_score += 1
            print(f"You're right! Current score: {total_score}")
            first = second
        else:
            print(f"Sorry, that's wrong. Final score is {total_score}")
            game_continue = False
    else:
        if compare_followers(first, second) == 0:
            total_score += 1
            print(f"You're right! Current score: {total_score}")
            first = first
        else:
            print(f"Sorry, that's wrong. Final score is {total_score}")
            game_continue = False


