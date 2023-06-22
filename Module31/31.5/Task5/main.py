from typing import List
import requests
import re

link = "http://www.columbia.edu/~fdc/sample.html"
# link = "https://coinmarketcap.com/"
find_list: List = list()


def cleaning(my_req):
    pattern = re.compile(r"<h3.*</h3>")
    str_list = pattern.findall(my_req.text)

    for i_elem in str_list:
        clear_pattern_start = re.compile(r"<h3 id=\"\w*\">|<h3>")
        clear_pattern_end = re.compile(r"</h3>")

        temp_str = clear_pattern_start.sub("", i_elem)
        temp_str = clear_pattern_end.sub("", temp_str)

        find_list.append(temp_str)

"""
Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта (они заключены в теги <h3>).
"""

req = requests.get(link)
if req.status_code == 200:
    cleaning(my_req=req)
    print("Найдено:", find_list)
else:
    print("Сайт не удалось спарсить!")




"""
Ожидаемый результат:
['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters', '4. Converting Plain Text to HTML', 
'5. Effects', '6. Lists', '7. Links', '8. Tables', '9. Viewing Your Web Page', '10. Installing Your Web Page on the 
Internet', '11. Where to go from here', '12. Postscript: Cell Phones']

Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.
"""
