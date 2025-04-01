steps = 0

while True:
    command = input()
    diff_steps = 0

    if command == "Going home":
        total_steps = int(input())
        steps += total_steps

        if steps >= 10_000:
            diff_steps = steps - 10_000
            print("Goal reached! Good job!")
            print(f"{diff_steps} steps over the goal!")
            break
        else:
            diff_steps = 10_000 - steps
            print(f"{diff_steps} more steps to reach goal.")
            break

    steps += int(command)

    if steps >= 10_000:
        diff_steps = steps - 10_000
        print("Goal reached! Good job!")
        print(f"{diff_steps} steps over the goal!")
        break