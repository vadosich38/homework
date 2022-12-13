count_family = int(input("Сколько человек в семье: "))
tree = dict()
num = 0
for i_branch in range(1, count_family):
    names = input("{} пара: ".format(i_branch)).split()
    if names[1] not in tree:
        tree[names[1]] = num
        num += 1

    if names[0] not in tree:
        tree[names[0]] = tree[names[1]] + 1
print("'Высота' каждого члена семьи:")
for name in sorted(tree):
    print(name, tree[name])


# print(tree)
# print(*tree, tree[*tree], sep="\n")

