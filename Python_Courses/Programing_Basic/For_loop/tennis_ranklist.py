from math import ceil, floor

number_tournaments = int(input())
starting_points = int(input())

wins = 0
point_from_tournaments = 0

for _ in range(number_tournaments):
    type_stage = input()

    if type_stage == "W":
        point_from_tournaments += 2000
        wins += 1
    elif type_stage == "F":
        point_from_tournaments += 1200
    elif type_stage == "SF":
        point_from_tournaments += 720

average_points = floor(point_from_tournaments / number_tournaments)
percent_wins = (wins / number_tournaments) * 100

print(f"Final points: {starting_points + point_from_tournaments}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")