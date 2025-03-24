actor_name = input()
points_from_academy = float(input())
number_judges = int(input())

for _ in range(number_judges):
    judge_name = input()
    points_from_judge = float(input())

    points_from_academy += (len(judge_name) * points_from_judge) / 2

    if points_from_academy > 1250.5:
        break

if points_from_academy > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points_from_academy:.1f} more!")