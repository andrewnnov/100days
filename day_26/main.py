
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

