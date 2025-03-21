budget = int(input())
season = input()
group_of_fishermen = int(input())

price_for_ship = 0

if season == "Spring":
    price_for_ship = 3000
    if group_of_fishermen <= 6:
        price_for_ship *= 0.90
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    elif group_of_fishermen <= 11:
        price_for_ship *= 0.85
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    else:
        price_for_ship *= 0.75
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
elif season == "Summer":
    price_for_ship = 4200
    if group_of_fishermen <= 6:
        price_for_ship *= 0.90
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    elif group_of_fishermen <= 11:
        price_for_ship *= 0.85
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    else:
        price_for_ship *= 0.75
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
elif season == "Autumn":
    price_for_ship = 4200
    if group_of_fishermen <= 6:
        price_for_ship *= 0.90
    elif group_of_fishermen <= 11:
        price_for_ship *= 0.85
    else:
        price_for_ship *= 0.75
elif season == "Winter":
    price_for_ship = 2600
    if group_of_fishermen <= 6:
        price_for_ship *= 0.90
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    elif group_of_fishermen <= 11:
        price_for_ship *= 0.85
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95
    else:
        price_for_ship *= 0.75
        if group_of_fishermen % 2 == 0:
            price_for_ship *= 0.95

total_price = abs(budget - price_for_ship)

if budget >= price_for_ship:
    print(f"Yes! You have {total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price:.2f} leva.")