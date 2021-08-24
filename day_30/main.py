# File not found
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["aasss"])

except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError("This is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Humans Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):

    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as error_message:
        print(f"Index {error_message} more than consist in array")
    except TypeError:
        print("Index must be an int type")

make_pie(2)


