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

    def update(self, i, j, value):
        if (i < 0 or i > len(self.data) - 1) or (j < 0 or j > len(self.data) - 1) or i > j:
            raise Exception('Invalid Parameter')
        for _i in range(i, j + 1):
            self.data[_i] = value


if __name__ == '__main__':
    data = [randint(0, 9999) for _ in list(range(10000))]
    m = 1000
    i, j = randint(0, 9999), randint(0, 9999)
    if i > j:
        i, j = j, i
    a = BaseLoopWithUpdate(data)
    import time

    start = time.time()
    for _ in range(m):
        a.update(i, j, randint(0, 9999))
    print(a.sum_range(2, 7498))
    end = time.time()
    print(end - start)
