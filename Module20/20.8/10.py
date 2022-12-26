def min_search(string, tpl):
    return min(len(string), len(tpl))

data1 = "abc"
data2 = (10, 20, 30, 40)

pairs = ((data1[i_elem], data2[i_elem])
        for i_elem in range(min_search(data1, data2)))

print(pairs)
for i_paar in pairs:
    print(i_paar)