total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
end_of_movies = True

while True:
    movie = input()

    if movie == "Finish":
        end_of_movies = True
        break

    places_in_room = int(input())
    tickets = 0


    while True:
        ticket_type = input()

        if ticket_type == "student":
            student_tickets += 1
            total_tickets += 1
            tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            total_tickets += 1
            tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            total_tickets += 1
            tickets += 1

        if ticket_type == "End" or tickets == places_in_room:
            percent_capacity = (tickets / places_in_room) * 100
            print(f"{movie} - {percent_capacity:.2f}% full.")
            break

if True:
    percent_student_tickets = (student_tickets / total_tickets) * 100
    percent_standard_tickets = (standard_tickets / total_tickets) * 100
    percent_kids_tickets = (kids_tickets / total_tickets) * 100
    print(f"Total tickets: {total_tickets}")
    print(f"{percent_student_tickets:.2f}% student tickets.")
    print(f"{percent_standard_tickets:.2f}% standard tickets.")
    print(f"{percent_kids_tickets:.2f}% kids tickets.")