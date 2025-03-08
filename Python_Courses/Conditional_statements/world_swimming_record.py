from math import  floor

world_record = float(input())
distance = float(input())
time_for_swim = float(input())

distance_for_swim = distance * time_for_swim
resistance_of_water = floor((distance / 15)) * 12.5
total_time = distance_for_swim + resistance_of_water
diff = total_time - world_record

if total_time < world_record:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")