yearly_tax_for_trainings = int(input())

sneakers = yearly_tax_for_trainings * 0.60
sweatshirt_and_shorts = sneakers * 0.80
ball = sweatshirt_and_shorts * 0.25
accessories = ball * 0.20

total_tax = yearly_tax_for_trainings + sneakers + sweatshirt_and_shorts + ball + accessories
print(total_tax)