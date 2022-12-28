old_prices = [120, 550, 410, 990]
discount = 0.15
new_prices = [int(product * (1 - discount)) for product in old_prices]
print(new_prices)