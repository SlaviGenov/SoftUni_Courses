width_space = int(input())
length_space = int(input())
height_space = int(input())

total_space = width_space * length_space * height_space

while True:
    command = input()

    if command == "Done":
        print(f"{total_space} Cubic meters left.")
        break

    total_space -= int(command)

    if total_space <= 0:
        print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
        break