first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number +1):
        text_current_number = str(current_number)
        sum_even_position = 0
        sum_odd_position = 0


        for index, digit in enumerate(text_current_number):
            if index % 2 == 0:
                sum_even_position += int(digit)
            else:
                sum_odd_position += int(digit)

        if sum_even_position == sum_odd_position:
            print(current_number, end=" ")