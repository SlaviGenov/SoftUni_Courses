town = input()
sells = float(input())

commission = 0
error_data = False

if town == "Sofia":
    if 0 <= sells <= 500:
        commission = sells * 0.05
    elif sells <= 1000:
        commission = sells * 0.07
    elif sells <= 10000:
        commission = sells * 0.08
    elif sells > 10000:
        commission = sells * 0.12
    else:
        error_data = True
elif town == "Varna":
    if 0 <= sells <= 500:
        commission = sells * 0.045
    elif sells <= 1000:
        commission = sells * 0.075
    elif sells <= 10000:
        commission = sells * 0.10
    elif sells > 10000:
        commission = sells * 0.13
    else:
        error_data = True
elif town == "Plovdiv":
    if 0 <= sells <= 500:
        commission = sells * 0.055
    elif sells <= 1000:
        commission = sells * 0.08
    elif sells <= 10000:
        commission = sells * 0.12
    elif sells > 10000:
        commission = sells * 0.145
    else:
        error_data = True
else:
    error_data = True

if not error_data:
    print(f"{commission:.2f}")
else:
    print("error")