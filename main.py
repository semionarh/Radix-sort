from random import randint

import pandas as pandas


def RadixSortCount(array):
    if len(array) == 0:
        return []
    countIterations = 0
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)]
        for x in array:
            countIterations += 1
            figure = x // 10 ** i % 10
            B[figure].append(x)
        array = []
        for k in range(rang):
            array = array + B[k]
    return countIterations

def RadixSort(array):
    if len(array) == 0:
        return []
    countIterations = 0
    length = len(str(max(array)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)]
        for x in array:
            countIterations += 1
            figure = x // 10 ** i % 10
            B[figure].append(x)
        array = []
        for k in range(rang):
            array = array + B[k]
    return array

def ArithmeticProgression():
    array_len = []
    length = 0
    array_count_iter = []
    for i in range(100):
        array = []
        length += 5
        for j in range(length):
            array.append(randint(0, 999))

        array_count_iter.append(RadixSortCount(array))
        array_len.append(length)

    data = dict(length=array_len, quantity=array_count_iter)
    df = pandas.DataFrame(data)
    df.to_csv(r'arithmetic.csv', sep=';', index=False)


def GeometricProgression():
    array_len = []
    length = 1
    array_count_iter = []
    for i in range(15):
        array = []
        length *= 2
        for j in range(length):
            array.append(randint(0, 999))

        array_count_iter.append(RadixSortCount(array))
        array_len.append(length)

    data = dict(length=array_len, quantity=array_count_iter)
    df = pandas.DataFrame(data)
    df.to_csv(r'geometric.csv', sep=';', index=False)
if __name__ == '__main__':
    ArithmeticProgression()
    GeometricProgression()