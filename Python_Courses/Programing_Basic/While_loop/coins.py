current_sum = float(input())

total_coins = 0
total_sum = int(current_sum * 100)

while total_sum >= 0:
    total_coins += 1

    if total_sum >= 200:
        total_sum -= 200
    elif total_sum >= 100:
        total_sum -= 100
    elif total_sum >= 50:
        total_sum -= 50
    elif total_sum >= 20:
        total_sum -= 20
    elif total_sum >= 10:
        total_sum -= 10
    elif total_sum >= 5:
        total_sum -= 5
    elif total_sum >= 2:
        total_sum -= 2
    elif total_sum >= 1:
        total_sum -= 1

    if total_sum == 0:
        print(total_coins)
        break