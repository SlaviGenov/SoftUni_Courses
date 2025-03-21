budget = float(input())
season = input()

type_of_vacantion = ""
destination = ""
cost_for_vacation = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_vacantion = "Camp"
        cost_for_vacation = budget * 0.30
    elif season == "winter":
        type_of_vacantion = "Hotel"
        cost_for_vacation = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_vacantion = "Camp"
        cost_for_vacation = budget * 0.40
    elif season == "winter":
        type_of_vacantion = "Hotel"
        cost_for_vacation = budget * 0.80
else:
    destination = "Europe"
    type_of_vacantion = "Hotel"
    cost_for_vacation = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_of_vacantion} - {cost_for_vacation:.2f}")
