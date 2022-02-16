student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_score = student_scores[key]
    if student_score >= 91: 
        student_grades[key] = "Outstanding"
    elif student_score >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_score >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    
#🚨 Don't change the code below 👇
print(student_grades)