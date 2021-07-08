import random
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
colors = ["red", "green", "black", "blue", "orange", "grey"]


def random_direction():
    list_of_directions = ["1", "2"]
    distance = random.randint(10, 20)
    print(distance)
    direction = random.choice(list_of_directions)
    print(direction)
    tim.forward(distance)
    if direction == "1":
        tim.right(90)
    elif direction == "2":
        tim.left(90)


for _ in range(1000):
    tim.color(random.choice(colors))
    tim.speed(300)
    tim.pensize(5)
    random_direction()

screen = Screen()
screen.exitonclick()