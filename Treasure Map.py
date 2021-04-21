row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do want to put the treasure? ")

x_position = int(position[0]) - 1
y_position = int(position[1]) - 1

map[y_position][x_position] = "X"


print(f"{row1}\n{row2}\n{row3}")
