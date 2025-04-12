floor = int(input())
rooms = int(input()) - 1
last_floor = floor

for floor in range(floor, 0, -1):
    for rooms in range(0, rooms + 1):
        if floor == last_floor:
            print(f"L{floor}{rooms}", end =" ")
        elif floor % 2 == 0:
            print(f"O{floor}{rooms}", end =" ")
        else:
            print(f"A{floor}{rooms}", end =" ")
    print()