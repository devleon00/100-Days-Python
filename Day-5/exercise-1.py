student_heights = input("Input a list of student heights ").split()
print(student_heights)
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_sum = 0
number_of_students = 0
for n in student_heights:
    total_sum += n
    number_of_students += 1

print(round((total_sum / number_of_students)))

