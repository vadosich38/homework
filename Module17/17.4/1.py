import random

original_prices = [random.randint(-400, 400) for _ in range(10)]
new_prices = original_prices[:]
for i in range(len(new_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли:",  sum(original_prices) - sum(new_prices))