starting_number = int(input())
final_number = int(input())
magic_number = int(input())
combinations = 0
is_found = False

for first_number in range(starting_number, final_number + 1):
    for second_number in range(starting_number, final_number + 1):
        combinations += 1
        if first_number + second_number == magic_number:
            current_combination = combinations
            is_found = True
            print(f"Combination N:{current_combination} ({first_number} + {second_number} = {magic_number})")
            break

    if is_found:
        break

if not is_found:
    print(f"{combinations} combinations - neither equals {magic_number}")