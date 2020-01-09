from random import randint, sample


class Node:
    def __init__(self, left=None, right=None, bound_l=None, bound_r=None, value=None, is_left=None, is_right=None):
        self.is_left = is_left
        self.is_right = is_right
        self.left = left
        self.right = right
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.value = value

    def __str__(self):

        if self.is_left:
            prefix = 'left'
        elif self.is_right:
            prefix = 'right'
        else:
            prefix = ''
        return f'{prefix}[{self.bound_l}-{self.bound_r}:{self.value}]'


class SegmentTree:
    """
    线段树
    """

    def __init__(self, data: list, merger: callable):
        self.data = data
        self._merger = merger
        self._root = self._build()

    @property
    def root(self):
        return self._root

    def _build(self):
        self._root = Node(bound_l=0, bound_r=len(self.data) - 1)
        return self._build_segment_tree(self._root)

    def _build_segment_tree(self, node):
        """
        在node节点上创建左边界为bound_l, 右边界为bound_r的segment_tree
        :param node:
        :return:
        """
        if node.bound_l == node.bound_r:
            node.value = self.data[node.bound_l]
            return node
        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        left_node = self._build_segment_tree(Node(bound_l=node.bound_l, bound_r=mid, is_left=True))
        right_node = self._build_segment_tree(Node(bound_l=mid + 1, bound_r=node.bound_r, is_right=True))
        node.left = left_node
        node.right = right_node
        node.value = self._merger(left_node.value, right_node.value)
        return node

    def get(self, index):
        if index < 0 or index > len(self.data) - 1:
            raise Exception('Invalid Parameter')
        return self.data[index]

    def print_tree(self):
        self._print_tree(self._root, 0, 18)

    def _print_tree(self, node, height, length):
        """
        打印树
        :param node:
        :param height:
        :param length:
        :return:
        """
        if node is None:
            return
        self._print_tree(node.left, height + 1, length)
        node_str = str(node)
        left_len = (length - len(node_str)) // 2
        right_len = length - len(node_str) - left_len
        res = " " * left_len + node_str + " " * right_len
        print(" " * height * length + res)
        self._print_tree(node.right, height + 1, length)

    def query(self, query_l, query_r):
        """
        线段树的查询
        :param query_l: 查询左边界
        :param query_r: 查询右边界
        :return:
        """
        if (query_l < 0 or query_l > len(self.data) - 1) or (
                query_r < 0 or query_r > len(self.data) - 1) or query_r < query_l:
            raise Exception('Invalid Parameter')

        return self._query(self._root, query_l, query_r)

    def _query(self, node, query_l, query_r):
        """
        在以node为根的segment的范围里搜索区间[query_l, query_r]的值
        :param node:
        :param query_l:
        :param query_r:
        :return:
        """
        if node.bound_l == query_l and node.bound_r == query_r:
            return node.value
        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        if query_l >= mid + 1:
            return self._query(node.right, query_l, query_r)
        elif query_r <= mid:
            return self._query(node.left, query_l, query_r)
        else:
            left_result = self._query(node.left, query_l, mid)
            right_result = self._query(node.right, mid + 1, query_r)
            return self._merger(left_result, right_result)

    def update(self, index, value):
        if index < 0 or index > len(self.data) - 1:
            raise Exception('Invalid Parameter')
        self.data[index] = value
        self._update_tree(self._root, index, value)

    def _update_tree(self, node, index, value):
        if node.bound_l == index and node.bound_r == index:
            node.value = value
            return node
        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        if index <= mid:
            node.left = self._update_tree(node.left, index, value)
        else:
            node.right = self._update_tree(node.right, index, value)

        node.value = self._merger(node.left.value, node.right.value)
        return node

    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    import time

    a = SegmentTree(data=list(range(10000)), merger=lambda x, y: x + y)
    start = time.time()
    m = 100
    for _ in range(m):
        for _i in range(1000, 2001):
            a.update(_i, randint(0, 9999))

    print(a.query(2, 9999))
    end = time.time()
    print(end - start)
