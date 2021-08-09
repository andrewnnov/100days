import turtle
import pandas
from turtle import Screen, Turtle


FONT = ("Arial", 11, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

write_turtle = Turtle()
write_turtle.hideturtle()
write_turtle.penup()
score = 0
game_is_on = True

while game_is_on:

    print(score)
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's?").title()

    state_of_us = pandas.read_csv("50_states.csv")
    list_of_state = state_of_us["state"].to_list()
    # print(list_of_state)


    if answer_state in list_of_state:
        score += 1
        guess_state = state_of_us[state_of_us.state == answer_state]
        # print(guess_state)
        x_cor = int(guess_state.x)
        # print(x_cor)
        y_cor = int(guess_state.y)
        # print(y_cor)
        write_turtle.setpos(x_cor, y_cor)
        write_turtle.write(answer_state, font=FONT)


