student_heights = input("Input a list of student heihgt ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

nuber_of_students = 0
sum_of_height = 0
for height in student_heights:
    sum_of_height += height
    nuber_of_students  += 1
    
aver_height = round(sum_of_height / nuber_of_students)
print(aver_height)
