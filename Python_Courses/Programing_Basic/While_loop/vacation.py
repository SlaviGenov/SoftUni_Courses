money_for_excursion = float(input())
own_money = float(input())

spending_days = 0
total_days = 0

while spending_days < 5:
    command = input()
    money = float(input())

    total_days += 1

    if command == "spend":
        own_money -= money
        if own_money < 0:
            own_money = 0
        spending_days += 1
    elif command == "save":
        own_money += money
        spending_days = 0

    if spending_days == 5:
        print("You can't save the money.")
        print(total_days)
        break

    if own_money >= money_for_excursion:
        print(f"You saved the money for {total_days} days.")
        break