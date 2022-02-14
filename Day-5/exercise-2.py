student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0
for scores in student_scores:
    if scores > max:
        max = scores

print(f"{max} is the highest score")