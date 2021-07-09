import random
import turtle as t
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
t.colormode(255)
tim.speed("fastest")



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(360):
    tim.color(random_color())
    tim.circle(200)
    tim.left(1)


screen = Screen()
screen.exitonclick()