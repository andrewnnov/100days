

with open("file1.txt") as file1_data:
    data_1 = file1_data.readlines()
    data_int_1 = [int(row.strip("\n")) for row in data_1]
    print(data_int_1)

with open("file2.txt") as file2_data:
    data_2 = file2_data.readlines()
    data_int_2 = [int(row.strip("\n")) for row in data_2]
    print(data_int_2)


if len(data_int_1) > len(data_int_2):
    result = [number for number in data_int_1 if number in data_int_2]
else:
    result = [number for number in data_int_2 if number in data_int_1]

print(result)