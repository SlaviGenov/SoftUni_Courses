best_player = ""
most_goals = 0
hat_trick = 0

while True:
    player = input()

    if player == "END":
        break

    goals = int(input())

    if goals > most_goals:
        best_player = player
        most_goals = goals

    if goals >= 3:
        hat_trick = 1

    if goals >= 10:
        break

print(f"{best_player} is the best player!")
if hat_trick == 1:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
elif hat_trick == 0:
    print(f"He has scored {most_goals} goals.")