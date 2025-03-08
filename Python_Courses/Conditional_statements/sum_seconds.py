first_sprinter_time = int(input())
second_sprinter_time = int(input())
third_sprinter_time = int(input())

total_time = first_sprinter_time + second_sprinter_time + third_sprinter_time

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")