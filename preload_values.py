from random import randint


class PreloadValues:
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


#      O(1)


if __name__ == '__main__':
    data = [randint(0, 9999) for _ in list(range(10000))]
    a = PreloadValues(data)
    import time

    start = time.time()
    print(a.sum_range(2, 7498))
    end = time.time()
    print(end - start)
