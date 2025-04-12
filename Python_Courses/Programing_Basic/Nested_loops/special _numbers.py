number = int(input())

for num in range(1_111, 10_000):

    is_special = True
    num_as_str = str(num)

    for digit in num_as_str:
        digit_as_int = int(digit)

        if digit_as_int == 0:
            is_special = False
            break

        if number % digit_as_int != 0:
            is_special = False
            break

    if is_special:
        print(num, end=" ")
