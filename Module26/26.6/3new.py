import os
from typing import Iterable
flag = False


def gen_files_path(search_obj: str = "homework", start_path: str = f"{os.path.sep}") -> Iterable[str]:
    global flag
    path_files = os.listdir(start_path)
    for i_obj_name in path_files:
        fact_path = os.path.join(start_path, i_obj_name)
        if i_obj_name == search_obj:
            yield fact_path
            print("Папка найдена!\nОткрываю содержимое папки:\n")
            in_search = os.listdir(fact_path)
            flag = True
            for i_obj in in_search:
                yield i_obj
            return
        
        if flag:
            return
        elif os.path.isdir(fact_path):
            new_dir = gen_files_path(search_obj=search_obj, start_path=fact_path)
            for l_obj in new_dir:
                print(l_obj)
        else:
            yield fact_path
    else:
        return


my_search = gen_files_path(search_obj="homework", start_path="/Users/vladyslav/Downloads")
for j_obj in my_search:
    print(j_obj)
