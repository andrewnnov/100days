
# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)


#import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(type(data))
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
data = pandas.read_csv("weather_data.csv")
#
# print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# average = data["temp"].mean()
# print(average)
#
# max_value = data["temp"].max()
# print(max_value)
#
# # get data in columns
# print(data["condition"])
# print(data.condition)

# det data in row

max_value = data.temp.max()
print(data[data.temp == max_value])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# How to create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data_student = pandas.DataFrame(data_dict)
print(data_student)
data_student.to_csv("new_data.csv")




