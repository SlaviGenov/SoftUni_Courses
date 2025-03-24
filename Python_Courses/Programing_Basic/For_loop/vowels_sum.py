text = input()

nominal = 0

for char in text:
    if char == "a":
        nominal += 1
    elif char == "e":
        nominal += 2
    elif char == "i":
        nominal += 3
    elif char == "o":
        nominal += 4
    elif char == "u":
        nominal += 5

print(nominal)