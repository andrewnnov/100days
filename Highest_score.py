student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

h_score = student_scores[0]
for max in student_scores:
    if max > h_score:
        h_score = max

print(h_score)            
