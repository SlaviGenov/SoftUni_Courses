import sys

max_number = -sys.maxsize

while True:
    command = input()
    if command == "Stop":
        break
    if int(command) > max_number:
        max_number = int(command)

print(max_number)