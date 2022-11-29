main_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
second_list2 = [1, 3, 1, 5, 3, 3]

main_list.extend(second_list)
counter = main_list.count(5)
print("В списке найдено цифру 5:", counter, "раза")
for _ in range(counter):
    main_list.remove(5)
print(main_list)
main_list.extend(second_list2)
counter = main_list.count(3)
print("В списке найдено цифру 3:", counter, "раза")
for _ in range(counter):
    main_list.remove(3)
print(main_list)