numbers = int(input())

left_sum = 0
right_sum = 0

for _ in range(numbers):
    left_sum += int(input())

for _ in range(numbers):
    right_sum += int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")