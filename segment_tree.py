from random import randint


class Node:
    def __init__(self, left=None, right=None, bound_l=None, bound_r=None, value=None, is_left=None, is_right=None):
        self.is_left = is_left
        self.is_right = is_right
        self.left = left
        self.right = right
        self.bound_l = bound_l
        self.bound_r = bound_r
        self.value = value
        self.lazy_tag = 0

    def __str__(self):

        if self.is_left:
            prefix = 'left'
        elif self.is_right:
            prefix = 'right'
        else:
            prefix = ''
        return f'{prefix}[{self.bound_l}-{self.bound_r}:{self.value}|lazy:{self.lazy_tag if self.lazy_tag else "False"}]'


class SegmentTree:
    """
    线段树
    """

    def __init__(self, data: list, merger: callable, lazy_push_down, lazy_tag_processor):
        self.data = data
        self._merger = merger
        self._lazy_push_down = lazy_push_down
        self._lazy_tag_processor = lazy_tag_processor
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
        mid = node.bound_l + (node.bound_r - node.bound_l) // 2  # (r + l) / 2
        left_node = self._build_segment_tree(Node(bound_l=node.bound_l, bound_r=mid, is_left=True))
        right_node = self._build_segment_tree(Node(bound_l=mid + 1, bound_r=node.bound_r, is_right=True))
        node.left = left_node
        node.right = right_node
        node.value = self._merger(left_node.value, right_node.value)  # left + right
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
        if node.lazy_tag:
            self._lazy_push_down(node)

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
        self._update(self._root, index, value)

    def _update(self, node, index, value):
        if node.bound_l == index and node.bound_r == index:
            node.value = value
            return node
        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        if index <= mid:
            node.left = self._update(node.left, index, value)
        else:
            node.right = self._update(node.right, index, value)

        node.value = self._merger(node.left.value, node.right.value)
        return node

    def update_segment(self, l, r, x):
        """
        更新区间
        """
        if (l < 0 or l > len(self.data) - 1) or (
                r < 0 or r > len(self.data) - 1) or r < l:
            raise Exception('Invalid Parameter')

        self._update_segment(self._root, l, r, x)

    def _update_segment(self, node, l, r, x):
        if node.bound_l == l and node.bound_r == r:
            self._lazy_tag_processor(node, l, r, x)
            return node

        mid = node.bound_l + (node.bound_r - node.bound_l) // 2
        if r <= mid:
            node.left = self._update_segment(node.left, l, r, x)

        elif l >= mid + 1:
            node.right = self._update_segment(node.right, l, r, x)
        else:
            node.left = self._update_segment(node.left, l, mid, x)
            node.right = self._update_segment(node.right, mid + 1, r, x)
        node.value = self._merger(node.left.value, node.right.value)
        return node

    def __len__(self):
        return len(self.data)


class ObjWithSegmentTree:
    def __init__(self, data):
        self.data = data
        self._segment_tree = SegmentTree(data, merger=self._merger, lazy_push_down=self._lazy_push_down,
                                         lazy_tag_processor=self._lazy_tag_processor)

    @staticmethod
    def _merger(x, y):
        raise NotImplementedError()

    @staticmethod
    def _lazy_push_down(node):
        raise NotImplementedError()

    @staticmethod
    def _lazy_tag_processor(node):
        raise NotImplementedError()

    @property
    def update(self):
        return self._segment_tree.update_segment

    @property
    def query(self):
        return self._segment_tree.query
