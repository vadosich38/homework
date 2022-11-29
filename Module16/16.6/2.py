class_a = list(range(160, 176, 2))
class_b = list(range(162, 180, 3))
class_a.extend(class_b)

def sort():
    min = 10e16
    for mult in range(len(class_a)):
        for num in range(0 + mult, len(class_a)):
            if class_a[num] < min:
                min = class_a[num]
                pos = num

        class_a[mult], class_a[pos] = class_a[pos], class_a[mult]
        min = 10e16
sort()
print(class_a)
