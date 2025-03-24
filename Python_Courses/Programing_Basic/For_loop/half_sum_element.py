import sys

numbers = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for _ in range(numbers):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

diff = abs(max_number - sum_numbers)

if max_number == diff:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff -=max_number
    print("No")
    print(f"Diff = {abs(diff)}")