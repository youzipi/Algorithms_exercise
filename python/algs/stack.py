# encoding=utf-8


class StackEmptyException(Exception): pass


class Stack(object):
    def __init__(self, data):
        self.stack = []
        if data is None:
            pass
        else:
            self.stack.extend(data)

    def push(self, item):
        self.stack = [item] + self.stack

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        else:
            raise StackEmptyException("overflow")

    def __str__(self, *args, **kwargs):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, offset):
        return self.stack[offset]

    def __getattr__(self, name):
        """
        sort(),append(),reverse()
        :param name:
        :return:
        """
        return getattr(self.stack, name)


if __name__ == '__main__':
    s = Stack([1, 2, 3])

    print(s)
    print(s)
    print(len(s))
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
