from random import randint
class PreloadValuesWithUpdate:
    def __init__(self, data):
        self.data = data
        self._sum = list(range(len(data) + 1))
        self._sum[0] = 0
        for i in range(1, len(self.data) + 1):
            self._sum[i] = self._sum[i - 1] + self.data[i - 1]

    def sum_range(self, l, r):
        if (l < 0 or l > len(self.data) - 1) or (r < 0 or r > len(self.data) - 1) or r < l:
            raise Exception('Invalid Parameter')
        return self._sum[r + 1] - self._sum[l]

    def update(self, index, value):
        if index < 0 or index > len(self.data) - 1:
            raise Exception('Invalid Parameter')
        self.data[index] = value
        for i in range(index + 1, len(self._sum)):
            self._sum[i] = self._sum[i - 1] + self.data[i - 1]


if __name__ == '__main__':
    import time
    a = PreloadValuesWithUpdate(data=list(range(100000)))
    m = 10
    start = time.time()
    a.update(783, randint(0, 9999))
    print(a.sum_range(2, 99990))
    end = time.time()
    print(end - start)
