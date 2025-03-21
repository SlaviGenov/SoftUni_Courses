hour_for_exam = int(input())
minutes_for_exam = int(input())
hour_for_arrive = int(input())
minutes_for_arrive = int(input())

time_for_exam = (hour_for_exam * 60) + minutes_for_exam
time_for_arrive = (hour_for_arrive * 60) + minutes_for_arrive

different_time = abs(time_for_arrive - time_for_exam)

hours = 0
minutes = 0

if time_for_arrive > time_for_exam:
    print("Late")
    if time_for_arrive <= 59 or different_time <= 59:
        print(f"{different_time} minutes after the start")
    else:
        hours = hour_for_arrive - hour_for_exam
        minutes = different_time - 60
        while minutes >= 60:
            minutes -= 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif time_for_arrive == time_for_exam:
    print("On time")
elif time_for_arrive < time_for_exam:
    if different_time <= 30:
        print("On time")
        print(f"{different_time} minutes before the start")
    elif different_time < 60:
        print("Early")
        print(f"{different_time} minutes before the start")
    else:
        print("Early")
        minutes = different_time - 60
        while different_time > 59:
            different_time -= 60
            hours += 1
        while minutes >= 60:
            minutes -= 60
        print(f"{hours}:{minutes:02d} hours before the start")