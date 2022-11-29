n = int(input("Введите сколько сотрудников в компании до сокращения: "))
salary_list = []
new_salary_list = []

for _ in range(n):
    salary = int(input("Введите зарплату очередного сотрудника: "))
    salary_list.append(salary)

for salary in salary_list:
    if salary != 0:
        new_salary_list.append(salary)

print("В компании осталось", len(new_salary_list), "сотрудников")
print("Зарплаты сотрудников:")
print(new_salary_list)

print("Максимальная зарплата:", max(new_salary_list))
print("Минимальная зарплата:", min(new_salary_list))