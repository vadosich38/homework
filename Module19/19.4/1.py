string = "Я! Есть. Грут?! Я, Грут и Есть."
signs = ".,;:!?"
signs_set = set(signs)
counter = 0
for symbol in string:
    if symbol in signs_set:
        counter += 1
print("Знаков припенания:", counter)