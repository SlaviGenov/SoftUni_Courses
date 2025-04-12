sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    command = input()
    if command == "stop":
        break

    if int(command) < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for i in range(2, int(command)):
        if int(command) % i == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime_numbers += int(command)
    else:
        sum_non_prime_numbers += int(command)

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")