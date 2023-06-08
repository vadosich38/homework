from functools import reduce
from typing import List, Union

sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]


def my_filter(count: int, sentence: str) -> int:
    return count + sentence.count("was")


print("Слово 'was' встречается в предложениях всего", reduce(my_filter, sentences, 0), "раз")
