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
    import time
    a = BaseLoopWithUpdate(list(range(10000)))
    start = time.time()
    m = 100
    for _ in range(m):
        for _i in range(1000, 2001):
            a.update(_i, randint(0, 9999))
    for _i in range(1000, 2001):
        print(a.sum_range(2, 9999))
    end = time.time()
    print(end - start)
