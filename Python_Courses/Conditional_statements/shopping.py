budget = float(input())
video_cards_needed = int(input())
processors_needed = int(input())
ram_memory_needed = int(input())

discount = 0
video_cards_price = video_cards_needed * 250
processors_price = (video_cards_price * 0.35) * processors_needed
ram_memory_price = (video_cards_price * 0.10) * ram_memory_needed
total_sum = video_cards_price + processors_price + ram_memory_price

if video_cards_needed > processors_needed:
    discount = total_sum * 0.15

diff = abs(budget - (total_sum - discount))

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")