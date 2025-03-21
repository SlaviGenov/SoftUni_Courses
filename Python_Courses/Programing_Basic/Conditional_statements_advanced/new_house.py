flowers_type = input()
count_flowers = int(input())
budget = int(input())

price = 0
if flowers_type == "Roses":
    price = count_flowers * 5
    if count_flowers > 80:
        price *= 0.90
elif flowers_type == "Dahlias":
    price = count_flowers * 3.80
    if count_flowers > 90:
        price *= 0.85
elif flowers_type == "Tulips":
    price = count_flowers * 2.80
    if count_flowers > 80:
        price *= 0.85
elif flowers_type == "Narcissus":
    price = count_flowers * 3
    if count_flowers < 120:
        price *= 1.15
elif flowers_type == "Gladiolus":
    price = count_flowers * 2.50
    if count_flowers < 80:
        price *= 1.20

total_price = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {flowers_type} and {total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price:.2f} leva more.")
