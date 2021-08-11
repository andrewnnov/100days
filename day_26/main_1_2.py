
name = "Angela"
new_list = [letter for letter in name]

print(new_list)

list_mult = [2 * el for el in range(1, 5)]
print(list_mult)

names_list = ['Tom', 'Alex', 'Andrew', 'Vital', 'John']

short_names = [name for name in names_list if len(name) < 5]
print(short_names)


long_names_uper = [name.upper() for name in names_list if len(name) >= 5]
print(long_names_uper)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)


even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)