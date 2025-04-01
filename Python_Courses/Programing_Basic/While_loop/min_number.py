import sys

min_number = sys.maxsize

while True:
    command = input()
    if command == "Stop":
        break
    if int(command) < min_number:
        min_number = int(command)

print(min_number)