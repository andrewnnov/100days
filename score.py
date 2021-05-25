student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student, score in student_scores.items():
    if score > 91 and score < 101:        
        student_grades[student]= "Outstanding"
    elif score > 80 and score < 91:        
        student_grades[student]= "Exceeds Expectations"
    elif score > 70 and score < 81:         
        student_grades[student]= "Acceptable"
    elif score <= 70:        
        student_grades[student]= "Fail"
print(student_grades)
