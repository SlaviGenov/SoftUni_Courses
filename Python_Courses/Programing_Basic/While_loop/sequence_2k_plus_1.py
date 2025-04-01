number = int(input())

current_number = 0

while current_number <= number:
    current_number = current_number * 2 + 1
    if current_number > number:
        break
    print(current_number)
