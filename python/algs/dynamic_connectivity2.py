# coding=utf-8
# from tabulate import tabulate
import os

from python.algs.dynamic_connectivity import UF


class QuickUnion(UF):
    def __init__(self, N):
        assert isinstance(N, int)
        self._count = N
        self.id = [i for i in range(N)]
        self.access_count = 0

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        else:
            min_val = min(p_id, q_id)
            max_val = max(p_id, q_id)
            self.id[max_val] = min_val

            self._count -= 1

    def find(self, p):
        # self.access_count += 1
        while self.not_match_root(p):
            p = self.get_root(p)
            # self.access_count += 1
        return p

    def get_root(self, p):
        p = self.id[p]
        return p

    def not_match_root(self, p):
        return p != self.id[p]


def process(file_path, clazz):
    with open(file_path, 'r') as f:
        n = int(f.readline())
        a = clazz(n)
        for line in f:
            points = [int(i) for i in line.split()]
            a.union(points[0], points[1])
        print(a.access_count)

    return a.count


if __name__ == '__main__':
    CUR_DIR = os.path.dirname(__file__)

    process(os.path.join(CUR_DIR, "test/largeUF.txt"), clazz=QuickUnion)
    # a.access_count = 15876112
