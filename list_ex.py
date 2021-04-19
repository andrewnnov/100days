import random

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(", ")

name_for_pay = names[random.randint(0, len(names) - 1)]
print(f"{name_for_pay} is going to buy the meal today!")
