def sum_range(data, i, j):
    _sum = 0
    for _i in range(i, j + 1):
        _sum += data[_i]
    return _sum
#  O(n)


if __name__ == '__main__':
    import time

    start = time.time()
    print(sum_range(list(range(100000)), 2, 74983))
    end = time.time()
    print(end - start)
