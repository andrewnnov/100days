from turtle import Turtle, Screen
import random
import string


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bets', prompt='Which turtle will the race? Enter a color: ')
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
is_race_on = False

for turtle in range(0, 6):
    name = "turtle" + str(turtle)
    name = Turtle(shape="turtle")
    name.penup()
    name.color(color[turtle])
    name.goto(-230, y)
    all_turtles.append(name)
    y = y + 40


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()