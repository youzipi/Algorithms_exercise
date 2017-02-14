# coding=utf-8
# from tabulate import tabulate


class UF(object):
    def __init__(self, N):
        assert isinstance(N, int)
        self._count = N
        self.id = [i for i in range(N)]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        else:
            min_val = min(p_id, q_id)
            max_val = max(p_id, q_id)
            for index, value in enumerate(self.id):
                if value == max_val:
                    self.id[index] = min_val
            self._count -= 1

    def find(self, p):
        return self.id[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    @property
    def count(self):
        return self._count

    def __str__(self, *args, **kwargs):
        s = "i  id\n"  # type:str
        for i, value in enumerate(self.id):
            s += "{i}   {id}\n".format(i=i, id=value)
        s += "connection_count={count}".format(count=self.count)
        return s


if __name__ == '__main__':
    a = UF(10)
    actions = [
        (9, 0),
        (3, 4),
        (5, 8),
        (7, 2),
        (2, 1),
        (5, 7),
        (0, 3),
        (4, 2)
    ]

    for p, q in actions:
        a.union(p, q)

    print(a)
