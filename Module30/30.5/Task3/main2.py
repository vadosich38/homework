from functools import reduce
from typing import List

sentences: List[str] = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]

print(reduce(lambda acc, sentence: acc + sentence.count("was"), sentences, 0))
