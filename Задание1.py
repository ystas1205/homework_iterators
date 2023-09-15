nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, data_list):
        self.data_list = data_list

    def __iter__(self):
        self.index_data = 0
        self.index_data1 = 0
        self.data_list1 = []
        return self

    def __next__(self):
        self.data = self.data_list[self.index_data]
        if self.index_data1 == len(self.data_list[self.index_data]):
            self.index_data += 1
            if self.index_data >= len(self.data_list):
                raise StopIteration
            self.data = self.data_list[self.index_data]
            self.index_data1 = 0
            self.data_list1.clear()
        self.data1 = self.data[self.index_data1]
        self.data_list1.append(self.data1)
        self.index_data1 += 1
        return self.data1


if __name__ == "__main__":
    for i in FlatIterator(nested_list):
        print(i)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
