price_for_excursion = float(input())
puzzles_needed = int(input())
talking_dolls_needed = int(input())
plush_bears_needed = int(input())
minions_needed = int(input())
trucks_needed = int(input())

total_toys = puzzles_needed + talking_dolls_needed + plush_bears_needed + minions_needed + trucks_needed
price_for_toys = puzzles_needed * 2.60 + talking_dolls_needed * 3 + plush_bears_needed * 4.10 + minions_needed * 8.20 + trucks_needed * 2

rent = 0

if total_toys >= 50:
    price_for_toys = price_for_toys * 0.75
    rent = price_for_toys * 0.10
else:
    rent = price_for_toys * 0.10

money_for_excursion = price_for_toys - rent
diff = abs(money_for_excursion - price_for_excursion)

if money_for_excursion >= price_for_excursion:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")