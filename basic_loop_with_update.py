from random import randint


class BaseLoopWithUpdate:
    def __init__(self, data):
        self.data = data

    def sum_range(self, i, j):
        if (i < 0 or i > len(self.data) - 1) or (j < 0 or j > len(self.data) - 1) or i > j:
            raise Exception('Invalid Parameter')
        _sum = 0
        for _i in range(i, j + 1):
            _sum += self.data[_i]
        return _sum

    def update(self, index, value):
        if index < 0 or index > len(self.data) - 1:
            raise Exception('Invalid Parameter')
        self.data[index] = value


if __name__ == '__main__':
    pass
