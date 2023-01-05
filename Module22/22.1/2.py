import os

folder = "Python"
print("Содержимое каталога {}".format(folder))

folder_path = os.path.abspath(os.path.join("..", "..", "..", "..", folder))
for i_elem in os.listdir(folder_path):
    print("      ", i_elem)

