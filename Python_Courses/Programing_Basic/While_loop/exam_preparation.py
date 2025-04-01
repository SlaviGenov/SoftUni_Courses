number_poor_grades = int(input())

last_problem = ""
poor_grades = 0
average_grade = 0
total_problems = 0

while True:
    problem = input()

    if problem == "Enough":
        average_grade = average_grade / total_problems
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {total_problems}")
        print(f"Last problem: {last_problem}")
        break

    current_grade = int(input())

    if current_grade <= 4:
        poor_grades +=1

    if poor_grades == number_poor_grades:
        print(f"You need a break, {poor_grades} poor grades.")
        break

    average_grade += current_grade
    total_problems += 1
    last_problem = problem