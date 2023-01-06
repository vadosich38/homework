nums = open("numbers.txt", "r", encoding="utf-8")
summ = 0
for i_num in nums:
    summ += int(i_num)
nums.close()
res = open("answer.txt", "w")
res.write(str(summ))
res.close()