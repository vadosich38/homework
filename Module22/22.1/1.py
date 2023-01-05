import os

folder = "access"
file = "admin.bat"

my_path = os.path.join("Skillbox", folder, file)
abs_path = os.path.abspath(file)

print("Относительный путь:", my_path)
print("Абсолютный путь:", abs_path)

