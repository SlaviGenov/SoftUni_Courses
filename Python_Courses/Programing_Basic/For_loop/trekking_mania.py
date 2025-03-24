number_group_climbers = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(number_group_climbers):
    peoples_in_group = int(input())
    if peoples_in_group <= 5:
        musala += peoples_in_group
    elif peoples_in_group <= 12:
        monblan += peoples_in_group
    elif peoples_in_group <= 25:
        kilimanjaro += peoples_in_group
    elif peoples_in_group <= 40:
        k2 += peoples_in_group
    else:
        everest += peoples_in_group

total_climbers = musala + monblan + kilimanjaro + k2 + everest

percent_musala = (musala / total_climbers) * 100
percent_monblan = (monblan / total_climbers) * 100
percent_kilimanjaro = (kilimanjaro / total_climbers) * 100
percent_k2 = (k2 / total_climbers) * 100
percent_everest = (everest / total_climbers) * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")