hours = 0
minutes = 0

for hours in range(0, 24):
    if hours > 23:
        hours = 0
    for minutes in range (0, 60):
        if minutes > 59:
            hours += 1
            minutes = 0

        print(f"{hours}:{minutes}")