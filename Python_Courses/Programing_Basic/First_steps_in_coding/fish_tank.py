length_of_fish_tank = int(input())
width_of_fish_tank = int(input())
height_of_fish_tank = int(input())
percent_for_accessories = float(input())

litters_of_water = length_of_fish_tank * width_of_fish_tank * height_of_fish_tank
percent = percent_for_accessories * 0.01

total_litters_of_water = (litters_of_water * 0.001) * (1 - percent)
print(total_litters_of_water)