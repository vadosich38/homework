import os

folder_name = input("Из какой папки собрать скрипты: ")
path = os.path.abspath(os.path.join("..", "..", "..", folder_name))
def grabber(way):
    for i_elem in os.listdir(way):
        if i_elem == ".DS_Store" or i_elem == "config" or i_elem == "ORIG_HEAD" or i_elem == ".gitignore" or i_elem == ".git":
            continue
        elif os.path.isdir(os.path.join(way, i_elem)):
            new_path = os.path.abspath(os.path.join(way, i_elem))
            grabber(new_path)
        else:
            file = open(os.path.join(way, i_elem), "r", encoding="utf-8")
            code = file.read()
            file.close()

            # print(os.path.join(way, i_elem))
            res_file = open("scripts.txt", "a")
            res_file.write(code)
            res_file.write("\n")
            res_file.write("*"*40)
            res_file.write("\n"*2)
            res_file.close()

grabber(path)
