def slicer(t, n):
    if n not in t:
        return ()
    if t.count(n) == 1:
        return t[t.index(n):]
    return t[t.index(n):t.index(n, t.index(n) + 1) + 1]

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 9))
