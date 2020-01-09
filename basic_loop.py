def sum_range(data, i, j):
    _sum = 0
    for _i in range(i, j + 1):
        _sum += data[_i]
    return _sum


if __name__ == '__main__':
    import time

    start = time.time()
    print(sum_range(list(range(10000)), 2, 9999))
    end = time.time()
    print(end - start)
