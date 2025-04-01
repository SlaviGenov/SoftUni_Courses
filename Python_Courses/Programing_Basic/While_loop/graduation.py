student_name = input()
total_grade = 0
current_class = 0
poor_grade = 0

while current_class < 12:
    grade = float(input())
    if grade >= 4.00:
        total_grade += grade
        current_class += 1
    else:
        poor_grade += 1

    if poor_grade == 2:
        print(f"{student_name} has been excluded at {current_class + 1} grade")
        break

    if current_class == 12:
        average_grade = total_grade / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")