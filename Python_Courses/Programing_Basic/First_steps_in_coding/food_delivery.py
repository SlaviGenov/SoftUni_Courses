number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegan_menu = int(input())

price_for_chicken_menu = number_of_chicken_menu * 10.35
price_for_fish_menu = number_of_fish_menu * 12.40
price_for_vegan_menu = number_of_vegan_menu * 8.15

total_price = (price_for_chicken_menu + price_for_fish_menu + price_for_vegan_menu)
dessert = total_price * 0.20
print(totcal_price + dessert + 2.50)