def is_polindrome(num_list):
    if list(reversed(num_list)) == num_list:
        return True
    else:
        return False

nums = []
new_nums = []
answer = []
n = int(input("Сколько чисел в последовательности: "))
for _ in range(n):
    n = int(input("Число: "))
    nums.append(n)

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_polindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print("Исходный список:", nums)
print("Нужно чисел для полиндропа", len(answer))
print("Список этих чисел:", answer)