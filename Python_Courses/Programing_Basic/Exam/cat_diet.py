percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

fats = ((percent_fats * 0.01) * total_calories) / 9
proteins = ((percent_proteins * 0.01) * total_calories) / 4
carbohydrates = ((percent_carbohydrates * 0.01) * total_calories) / 4

total_grams_elements = fats + proteins + carbohydrates
calories_per_gram_food = total_calories / total_grams_elements
water = ((percent_water * 0.01) * calories_per_gram_food)
calories = calories_per_gram_food - water
print(f"{calories:.4f}")