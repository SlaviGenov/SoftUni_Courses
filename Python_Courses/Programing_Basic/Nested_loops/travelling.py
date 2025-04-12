saved_money = 0

while True:
    destination = input()

    if destination == "End":
        break

    budget = float(input())

    while True:
        transaction = float(input())
        saved_money += transaction

        if saved_money >= budget:
            saved_money = 0
            print(f"Going to {destination}!")
            break