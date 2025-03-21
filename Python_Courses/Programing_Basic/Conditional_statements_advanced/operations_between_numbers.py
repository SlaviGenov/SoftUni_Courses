first_number = int(input())
second_number = int(input())
operator_type = input()

result = 0
even_or_odd = ""
operator = ""

if operator_type == "+":
    operator = "+"
    result = first_number + second_number
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator_type == "-":
    operator = "-"
    result = first_number - second_number
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator_type == "*":
    operator = "*"
    result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = "even"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
    else:
        even_or_odd = "odd"
        print(f"{first_number} {operator} {second_number} = {result} - {even_or_odd}")
elif operator_type == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        operator = "/"
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
elif operator_type == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        operator = "%"
        result = first_number % second_number
        print(f"{first_number} % {second_number} = {result}")
