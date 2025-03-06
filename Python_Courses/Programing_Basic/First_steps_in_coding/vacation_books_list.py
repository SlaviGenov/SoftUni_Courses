import math

number_of_pages_in_current_book = int(input())
pages_tobe_read_for_one_hour = int(input())
number_of_days_needed_to_read_book = int(input())

hours_needed_for_read_one_book = number_of_pages_in_current_book // pages_tobe_read_for_one_hour
days_for_read_book = hours_needed_for_read_one_book / number_of_days_needed_to_read_book

print(days_for_read_book)