count_pockets = int(input("Введите количество пакетов: "))
bytes_list = []
decode_list = []
counter_bad_pockets = 0

for pockets in range(count_pockets):
    print("\nПакет номер", pockets+1)
    for i_byte_num in range(4):
        print("Байт номер", i_byte_num+1, end = " ")
        byte = int(input())
        bytes_list.append(byte)

    if bytes_list.count(-1) <= 1:
        decode_list.extend(bytes_list)
    else:
        counter_bad_pockets += 1
        print("Много ошибок в пакете.")

        bytes_list = []

print("Полученное сообщение:", decode_list)
print("Кол-во ошибок в сообщении:", decode_list.count(-1))
print("Кол-во потерянных пакетов:", counter_bad_pockets)