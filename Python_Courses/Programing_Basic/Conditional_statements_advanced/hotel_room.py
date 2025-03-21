mount_type = input()
count_nights = int(input())

price_for_studio = 0
price_for_apartment = 0

if mount_type == "May" or mount_type == "October":
    if count_nights <= 7:
        price_for_studio = count_nights * 50
        price_for_apartment = count_nights * 65
    elif count_nights <= 14:
        price_for_studio = (count_nights  * 50) * 0.95
        price_for_apartment = count_nights * 65
    else:
        price_for_studio = (count_nights * 50) * 0.70
        price_for_apartment = (count_nights * 65) * 0.90
elif mount_type == "June" or mount_type == "September":
    if count_nights <= 14:
        price_for_studio = count_nights * 75.20
        price_for_apartment = count_nights * 68.70
    else:
        price_for_studio = (count_nights * 75.20) * 0.80
        price_for_apartment = (count_nights * 68.70) * 0.90
elif mount_type == "July" or mount_type == "August":
        if count_nights <= 14:
            price_for_studio = count_nights * 76
            price_for_apartment = count_nights * 77
        else:
            price_for_studio = count_nights * 76
            price_for_apartment = (count_nights * 77) * 0.90

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")