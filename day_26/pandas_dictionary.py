import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


students_data_frame = pandas.DataFrame(student_dict)
# print(students_data_frame)


# loop through a data frame
for (key, value) in students_data_frame.items():
    print(key)

# Loop through rows of a data frame

for (index, row) in students_data_frame.iterrows():
    print(row.student)