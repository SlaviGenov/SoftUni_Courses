product = input()
town = input()
quantity = float(input())

price = 0
if town == "Sofia":
    match product:
        case "coffee":
            price = 0.50
        case "water":
            price = 0.80
        case "beer":
            price = 1.20
        case "sweets":
            price = 1.45
        case "peanuts":
            price = 1.60
elif town == "Plovdiv":
    match product:
        case "coffee":
            price = 0.40
        case "water":
            price = 0.70
        case "beer":
            price = 1.15
        case "sweets":
            price = 1.30
        case "peanuts":
            price = 1.50
elif town == "Varna":
    match product:
        case "coffee":
            price = 0.45
        case "water":
            price = 0.70
        case "beer":
            price = 1.10
        case "sweets":
            price = 1.35
        case "peanuts":
            price = 1.55

total_price = price * quantity
print(total_price)