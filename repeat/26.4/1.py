class CountIterator:
    cur_val = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cur_val += 1
        return self.cur_val - 1


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
