numbers = int(input())

sum_odd_position = 0
sum_even_position = 0
numbers_counter = 0

for _ in range(numbers):

    current_number = int(input())
    numbers_counter += 1

    if numbers_counter % 2 == 0:
        sum_even_position += current_number
    else:
        sum_odd_position += current_number

diff = abs(sum_even_position - sum_odd_position)

if sum_odd_position == sum_even_position:
    print(f"Yes")
    print(f"Sum = {sum_even_position}")
else:
    print(f"No")
    print(f"Diff = {diff}")