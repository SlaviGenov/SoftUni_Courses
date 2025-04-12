number = int(input())
number_as_string = str(number)

result = 0

index_0 = number_as_string[2]
index_1 = number_as_string[1]
index_2 = number_as_string[0]
multiplier_1 = int(index_0)
multiplier_2 = int(index_1)
multiplier_3 = int(index_2)

for first_number in range(1, multiplier_1 + 1):
    for second_number in range(1, multiplier_2 + 1):
        for third_number in range(1, multiplier_3 + 1):
            result = first_number * second_number * third_number
            print(f"{first_number} * {second_number} * {third_number} = {result};")