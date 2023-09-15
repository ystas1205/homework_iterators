nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(value):
    data_index = 0
    data_index1 = 0
    list_data = []
    while data_index < len(nested_list):
        data = value[data_index]
        data1 = data[data_index1]
        list_data.append(data1)
        data_index1 += 1
        if data_index1 == len(data):
            data_index += 1
            data_index1 = 0
            list_data.clear()
        yield data1

    # def flat_generator1(value):
    # for i in value:
    #   for j in i:
    #      yield j


if __name__ == "__main__":
    for item in flat_generator(nested_list):
        print(item)


