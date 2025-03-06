nylon = int(input())
paint = int(input())
thinner = int(input())
hours_needed_for_workers = int(input())

price_for_nylon = (nylon + 2) * 1.50
price_for_paint = (paint * 1.1) * 14.50
price_for_thinner = thinner * 5
bags_price = 0.40

total_material_price = price_for_nylon + price_for_paint + price_for_thinner + bags_price
workers_wages = (total_material_price * 0.30) * hours_needed_for_workers

print(workers_wages + total_material_price)


