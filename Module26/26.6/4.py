from typing import Iterable


def qsequence(s: list) -> Iterable[int]:
    while True:
        try:
            q = s[-s[-1]] + s[-s[-2]]
            s.append(q)
            yield q
        except IndexError:
            return


for i_num in qsequence([1, 3]):
    print(i_num)
