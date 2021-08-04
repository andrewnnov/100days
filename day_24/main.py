file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()


with open('my_file.txt') as file:
    contents = file.read()
    print(contents)


# use write mode w
# use append a
with open('my_file.txt', mode="a") as file:
    file.write("\nNext text.")


with open("new_file.txt", mode='w') as file:
    file.write("\nI am created")

