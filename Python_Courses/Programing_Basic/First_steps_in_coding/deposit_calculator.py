deposit = float(input())
mounts_for_deposit = int(input())
year_percent_interest = float(input())

percent_for_deposit = deposit * (year_percent_interest * 0.01)
interest_for_one_mount = percent_for_deposit / 12
total_sum = deposit + mounts_for_deposit * interest_for_one_mount
print(total_sum)
