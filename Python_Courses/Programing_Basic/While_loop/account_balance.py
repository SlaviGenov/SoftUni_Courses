account_balance = 0
command = ""

while command != "NoMoreMoney":
    command = input()
    if command == "NoMoreMoney":
        print(f"Total: {account_balance:.2f}")
        break
    if float(command) < 0:
        print(f"Invalid operation!")
        print(f"Total: {account_balance:.2f}")
        break
    account_balance += float(command)
    print(f"Increase: {float(command):.2f}")