#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["name1", "name2", "name3"])
table.add_column("Type", ["fire", "water", "ice"])
table.align = "l"
print(table)

