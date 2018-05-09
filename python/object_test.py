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


class Solution:
    def gen(self, A):
        store = Store(A)
        return store


if __name__ == '__main__':
    s = Solution()
    print(s.multiply(A=[1, 2, 0, 4, 5]))
    print(s.multiply(A=[1, 2, 3, 4, 5]))
