from random import randint

from segment_tree import ObjWithSegmentTree


class SumMachine(ObjWithSegmentTree):

    @staticmethod
    def _merger(x, y):
        return x + y

    @staticmethod
    def _lazy_push_down(node):
        if node.bound_l == node.bound_r:
            return
        node.left.value += (node.left.bound_r - node.bound_l + 1) * node.lazy_tag
        node.left.lazy_tag += node.lazy_tag

        node.right.value += (node.right.bound_r - node.right.bound_l + 1) * node.lazy_tag
        node.right.lazy_tag += node.lazy_tag

        node.lazy_tag = 0

    @staticmethod
    def _lazy_tag_processor(node, l, r, x):
        node.value += (r - l + 1) * x
        node.lazy_tag += x


if __name__ == '__main__':

    data = [randint(0, 99999) for _ in list(range(100000))]
    m = 1000
    i, j = randint(0, 99999), randint(0, 99999)
    if i > j:
        i, j = j, i

    sum_machine = SumMachine(data)
    import time

    start = time.time()
    for _ in range(m):
        sum_machine.update(i, j, randint(0, 99999))
    print(sum_machine.query(2, 74983))
    end = time.time()
    print(end - start)
