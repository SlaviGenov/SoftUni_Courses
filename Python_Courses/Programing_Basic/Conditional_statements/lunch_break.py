from math import ceil

series_name = input()
duration_episode = int(input())
lunch_break = int(input())

lunch_time = lunch_break / 8
relax_time = lunch_break / 4
left_time = lunch_break - lunch_time - relax_time
diff = abs(duration_episode - left_time)

if left_time >= duration_episode:
    print(f"You have enough time to watch {series_name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(diff)} more minutes.")