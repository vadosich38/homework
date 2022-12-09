incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
summ = 0

for res in incomes.values():
    summ += res

print("Общая сумма дохода за год:", summ)
print("Меньше всех доход принес: grapefruit", ", доход составил:", incomes.pop("grapefruit"))
print("Итоговый словарь:", incomes)