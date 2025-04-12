number_of_peoples_in_jury = int(input())
counter_presentations = 0
total_grades = 0

while True:
    presentation = input()

    if presentation == "Finish":
        grade = total_grades / counter_presentations
        print(f"Student's final assessment is {grade:.2f}.")
        break

    average_grade = 0

    for current_jury in range(1, number_of_peoples_in_jury + 1):

        current_grade = float(input())
        average_grade += current_grade
        total_grades += current_grade
        counter_presentations += 1

        if  current_jury == number_of_peoples_in_jury:
            grade = average_grade / number_of_peoples_in_jury
            print(f"{presentation} - {grade:.2f}.")