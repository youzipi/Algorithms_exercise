"""
encoding=utf-8
_author = youzipi
date = 17/11/20
"""


# -*- coding:utf-8 -*-


class Store:
    """
    for oj
    """
    left = {}
    right = {}
    origin = []
    length = 0

    def __init__(self, origin):
        self.origin = origin
        self.length = len(origin)
        # self.left = {}
        # self.right = {}

    def left_product(self, index):
        if index < 0:
            return 1
        val = self.left.get(index)
        if val is None:
            val = self.origin[index] * self.left_product(index - 1)
            self.left.update({index: val})
        return val

    def right_product(self, index):
        if index > (self.length - 1):
            return 1
        val = self.right.get(index)
        if val is None:
            val = self.origin[index] * self.right_product(index + 1)
            self.right.update({index: val})
        return val


class Solution:
    def multiply(self, A):
        store = Store(A)
        B = []
        for index, val in enumerate(A):
            b = store.left_product(index - 1) * store.right_product(index + 1)
            B.append(b)
        return B


if __name__ == '__main__':
    s = Solution()
    print(s.multiply(A=[1, 2, 0, 4, 5]))
    print(s.multiply(A=[1, 2, 3, 4, 5]))
