# coding=utf-8
# from tabulate import tabulate
import copy
import os

from python.algs.dynamic_connectivity2 import QuickUnion


class WeightedQuickUnionUF(QuickUnion):
    def __init__(self, N):
        assert isinstance(N, int)
        self._count = N
        self.id = [i for i in range(N)]
        self.sz = [i for i in range(N)]
        self.access_count = 0

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        else:

            if self.sz[p_root] < self.sz[q_root]:
                min_root = p_root
                max_root = q_root
            else:
                min_root = q_root
                max_root = p_root

            self.id[min_root] = max_root
            self.sz[max_root] += self.sz[min_root]

            self._count -= 1


def process(file_path, clazz):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        # print("number=", n)
        a = clazz(n)
        for line in f:
            points = [int(i) for i in line.split()]
            p = points[0]
            q = points[1]
            a.union(p, q)
        print(a.access_count)
    return a.count


if __name__ == '__main__':
    CUR_DIR = os.path.dirname(__file__)

    process(os.path.join(CUR_DIR, "test/largeUF.txt"), clazz=WeightedQuickUnionUF)
    # a.access_count = 9722742
