# encoding=utf-8
# _author = youzipi
# date = 16/9/28
"""
refer: http://stackoverflow.com/a/39089983/3337452
"""
from python.algs.stack import Stack


class TwoStackQueue(object):
    in_stack = Stack([])
    out_stack = Stack([])

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if len(self.out_stack) > 0:
            return self.out_stack.pop()
        else:
            while len(self.in_stack) > 0:
                item = self.in_stack.pop()
                self.out_stack.push(item)
            return self.out_stack.pop()

    def __str__(self, *args, **kwargs):
        return "queue={queue}\n" \
               "in_stack={in_stack}\n" \
               "out_stack={out_stack}\n" \
            .format(queue=(self.out_stack[:], self.in_stack[::-1]),
                    in_stack=self.in_stack,
                    out_stack=self.out_stack
                    )

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)


if __name__ == '__main__':
    q = TwoStackQueue()

    list(map(lambda i: q.enqueue(i),range(5)))

    print(q)
    q.dequeue()
    print(q)

    q.enqueue(12)
    q.enqueue(13)
    print(q)
    q.dequeue()
    q.dequeue()
    print(q)


