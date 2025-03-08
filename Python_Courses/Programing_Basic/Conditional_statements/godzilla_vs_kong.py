budget_for_movie = float(input())
number_of_statists = int(input())
price_for_dress_per_statist = float(input())

price_for_decoration = budget_for_movie * 0.10
taxes = number_of_statists * price_for_dress_per_statist

discount_for_dressing = 0

if number_of_statists > 150:
    discount_for_dressing = taxes * 0.10

total_sum = price_for_decoration + (taxes - discount_for_dressing)

diff = abs(total_sum - budget_for_movie)

if total_sum > budget_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")