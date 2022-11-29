goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input("Введите название поступившего фрукта: ")
price = float(input("Введите цену товара: "))
tax = 1.08

new_good = [fruit_name, price]
goods.append(new_good)

for good in range(len(goods)):
    goods[good][1] = round(goods[good][1] * tax, 2)

print(goods)