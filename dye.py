from segment_tree import ObjWithSegmentTree
from random import randint

BLUE = 1
YELLOW = 2
RED = 3
GREEN = 4


class DyeWall(ObjWithSegmentTree):
    """
    染色墙
    """

    @staticmethod
    def _merger(x, y):
        return set.union(x, y)

    @staticmethod
    def _lazy_tag_processor(node, l, r, x):
        node.value = {x}
        node.lazy_tag += 1

    @staticmethod
    def _lazy_push_down(node):
        if node.bound_l == node.bound_r:
            return

        node.left.value = node.value
        node.left.lazy_tag += node.lazy_tag

        node.right.value = node.value
        node.right.lazy_tag += node.lazy_tag

        node.lazy_tag = 0

    def query_color_numbers(self, i, j):
        return len(self.query(i, j))

    @property
    def dye(self):
        return self.update


if __name__ == '__main__':
    data = [{randint(BLUE, GREEN)} for _ in list(range(100000))]
    m = 1000
    i, j = randint(0, 99999), randint(0, 99999)
    if i > j:
        i, j = j, i
    dye_wall = DyeWall(data)
    import time

    start = time.time()
    for _ in range(m):
        dye_wall.dye(i, j, randint(BLUE, GREEN))
    # print(dye_wall.query_color_numbers(0, len(data) - 1))
    print(dye_wall.query_color_numbers(2, 74983))
    end = time.time()
    print(end - start)
