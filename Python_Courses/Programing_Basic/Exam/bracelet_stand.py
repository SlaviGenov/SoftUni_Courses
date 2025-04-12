sells = float(input())
money_earned = float(input())
expenses = float(input())
price_for_gift = float(input())

saved_money = ((sells * 5) + (money_earned * 5) - expenses)
total = saved_money - price_for_gift

if total >= 0:
    print(f"Profit: {saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {abs(total):.2f} BGN.")