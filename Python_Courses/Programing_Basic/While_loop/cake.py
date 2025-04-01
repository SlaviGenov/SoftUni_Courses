width_cake = int(input())
length_cake = int(input())

pieces_cake = width_cake * length_cake

while True:
    command = input()

    if command == "STOP":
        print(f"{pieces_cake} pieces are left.")
        break

    pieces_cake -= int(command)

    if pieces_cake <= 0:
        print(f"No more cake left! You need {abs(pieces_cake)} pieces more.")
        break