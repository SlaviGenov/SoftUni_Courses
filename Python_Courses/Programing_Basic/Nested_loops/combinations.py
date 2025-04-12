number_one = 0
number_two = 0
number_tree = 0
combinations = 0
input_number = int(input())

for number_one in range(0, input_number + 1):
    for number_two in range(0, input_number + 1):
        for number_tree in range(0, input_number + 1):
            total_combination = number_one + number_two + number_tree
            if total_combination == input_number:
                combinations += 1

print(combinations)