from segment_tree import SegmentTree
from random import randint

BLUE = 1
YELLOW = 2
RED = 3
GREEN = 4

class DyeWall:
    """
    染色墙
    """

    def __init__(self, data):
        self.data = data
        self._segment_tree = SegmentTree(self.data, merger=lambda x, y: len(set.union(x, y)))
        self._segment_tree.lazy_push_down = self._lazy_push_down

    def dye(self, i, j, color):
        self._dye(self._segment_tree.root, i , j, color)

    def _dye(self, node, l, r, color):
        if node.bound_l == l and node.bound_r == r:
            node.value = {color}
            node.lazy_tag += 1
            return node

        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        if r <= mid:
            node.left = self._dye(node.left, l, r, {color})

        elif l >= mid + 1:
            node.right = self._dye(node.right, l, r, {color})
        else:
            node.left = self._dye(node.left, l, mid, {color})
            node.right = self._dye(node.right, mid + 1, r, {color})
        node.value = self._segment_tree._merger(node.left.value, node.right.value)
        return node

    @staticmethod
    def _lazy_push_down(node):

        if node.bound_l == node.bound_r:
            return

        node.left.value = {node.color}
        node.left.lazy_tag += node.lazy_tag

        node.right.value = {node.color}
        node.right.lazy_tag += node.lazy_tag

        node.lazy_tag = 0


    def query_color_numbers(self, i, j):
        return len(self._segment_tree.query(i, j))


if __name__ == '__main__':
    pass
