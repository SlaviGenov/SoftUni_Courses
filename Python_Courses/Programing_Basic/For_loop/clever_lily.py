age = int(input())
price_for_washing_machine = float(input())
price_for_one_toy = int(input())

money = 0
toys = 0
brother_steal = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += (birthday // 2) * 10
        brother_steal += 1
    else:
        toys += 1

total_money = (money + (toys * price_for_one_toy)) - brother_steal
diff = abs(total_money - price_for_washing_machine)

if total_money >= price_for_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")