number_packages_pens = int(input())
number_packages_markers = int(input())
litters_of_preparation = int(input())
percent_discount = int(input())

price_for_pens = number_packages_pens * 5.80
price_for_markers = number_packages_markers * 7.20
price_for_preparation = litters_of_preparation * 1.20
total_discount = percent_discount * 0.01

price_for_all_products = price_for_pens + price_for_markers + price_for_preparation
total_price = price_for_all_products * total_discount

print(price_for_all_products - total_price)