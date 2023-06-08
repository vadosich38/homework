from functools import reduce
from typing import List, Union

sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]


def my_filter(elem1: Union[int, str], elem2: str) -> int:
    if type(elem1) == str:
        counter = 0
        my_list = elem1.split()
        for word in my_list:
            if word == "was":
                counter += 1
    else:
        counter = elem1

    my_list = elem2.split()
    for word in my_list:
        if word == "was":
            counter += 1

    return counter


print("Слово 'was' встречается в предложениях всего", reduce(my_filter, sentences), "раз")
