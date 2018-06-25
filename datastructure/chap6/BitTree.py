# 二叉树的list实现,树有递归的性质

# 空树用None表示
# 非空二叉树有三个元素，用表[d,l,r]表示

class SubtreeIndexError(ValueError):
    pass


class TreeNode():
    def __init__(self, data, sub=[]):
        self._data = data
        self._subtrees = list(sub)

    def __str__(self):
        return 'TreeNode {0} {1}'.format(self._data, self._subtrees)


class BitTree():
    def __init__(self, data=None, left=None, right=None):
        self._root = [data, left, right]

    def is_Empty(self):
        return self._root[0] == None

    def root(self):
        return self._root[0]

    def left(self):
        return self._root[1]

    def right(self):
        return self._root[2]

    def set_Root(self, data):
        self._root[1] = data

    def set_Left(self, data):  # 这里的data可能是一个值，也可能是一个树
        self._root[1] = data

    def set_Right(self, data):  # 同上
        self._root[2] = data

    def __str__(self):
        return '[{0},{1},{2}]'.format(self._root[0], self._root[1], self._root[2])

#
# t1 = BitTree(1, BitTree(2, BitTree(4, 5, 6), 9), BitTree(3))
# print(t1)
