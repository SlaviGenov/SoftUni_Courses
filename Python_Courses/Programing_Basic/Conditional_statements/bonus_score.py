number = int(input())

bonus_points = 0
total_points = 0

if number <= 100:
   bonus_points += 5
elif number < 1000:
   bonus_points += number * 0.20
else:
    bonus_points += number * 0.10

if number % 2 == 0:
    bonus_points += 1

lastDigit = int(repr(number)[-1])
if lastDigit == 5:
    bonus_points += 2

total_points = number + bonus_points
print(bonus_points)
print(total_points)