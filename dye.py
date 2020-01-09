from segment_tree import SegmentTree
from random import randint

BLUE = 1
YELLOW = 2
RED = 3
GREEN = 4
GRAY = 5


class DyeWall:
    """
    染色墙
    """

    def __init__(self, data):
        self.data = data
        self._segment_tree = SegmentTree(self.data, merger=lambda x, y: set.union(x, y))

    def dye(self, i, j):
        for _i in range(i, j + 1):
            self._segment_tree.update(_i, {randint(BLUE, GRAY)})

    def query_color_numbers(self, i, j):
        return len(self._segment_tree.query(i, j))


if __name__ == '__main__':
    # 随机初始化
    initial_data = [{randint(BLUE, GRAY)} for _ in range(10000)]
    length = len(initial_data)
    # 染色次数
    m = 50

    dye_wall = DyeWall(initial_data)
    i = 3148
    j = 3151

    for _i in range(m):
        dye_wall.dye(i, j)

    print(dye_wall.query_color_numbers(i, j))
    print(dye_wall.query_color_numbers(0, 9999))
