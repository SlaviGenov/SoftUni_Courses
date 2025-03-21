days = int(input())
room_type = input()
rating = input()

nights = days - 1
room = ""
price = 0
discount = 0

if room_type == "room for one person":
    price = nights * 18
    discount = price
elif room_type == "apartment":
    price = nights * 25
    if days < 10:
         discount = price * 0.70
    elif days <= 15:
         discount = price * 0.65
    else:
         discount = price * 0.50
elif room_type == "president apartment":
    price = nights * 35
    if days < 10:
        discount = price * 0.90
    elif days <= 15:
        discount = price * 0.85
    else:
        discount = price * 0.80

if rating == "positive":
    discount *= 1.25
elif rating == "negative":
    discount *= 0.90

print(f"{discount:.2f}")