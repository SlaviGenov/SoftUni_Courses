days = int(input())

total_litters_rakia = 0
total_degrees = 0

for days in range(1, days + 1):
    litters_rakia = float(input())
    degrees = float(input())
    total_litters_rakia += litters_rakia
    total_degrees += litters_rakia * degrees

total_sum = total_degrees / total_litters_rakia

print(f"Liter: {total_litters_rakia:.2f}")
print(f"Degrees: {total_sum:.2f}")

if total_sum < 38:
    print("Not good, you should baking!")
elif total_sum < 42:
    print("Super!")
else:
    print("Dilution with distilled water!")