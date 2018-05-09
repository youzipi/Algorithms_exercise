"""
encoding=utf-8
_author = youzipi
date = 17/11/23
"""

"""
题目描述 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.length = len(pattern)
        self.p_i = 0

    def p(self, index):
        if index == self.length:
            raise ValueError('out of range')
        return self.pattern[index]

    def match_item(self, w):
        p = self.p(self.p_i)
        if p == w:
            self.p_i += 1
            return True
        elif p == '.':
            self.p_i += 1
            return True
        elif p == '*':
            if self.p(self.p_i - 1) == w:
                return True
            elif self.p(self.p_i + 1) == w:
                self.p_i += 2
                return True


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        temp = ''
        p_i = 0
        length = len(pattern)
        for index, i in enumerate(s):
            p = pattern[p_i]
            if p == '*':
                if pattern[p_i - 1] == i:
                    continue
                elif (p_i + 1) < length and pattern[p_i + 1] == i:
                    p_i += 2
                    continue
            elif (p_i + 1) < length and pattern[p_i + 1] == '*':
                p_i += 1
                continue
            else:
                return False
        if p_i == length:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()

    # print(s.match('aaa', 'a.a'))
    print(s.match('aaa', 'ab*ac*a'))
    # print(s.match('aaa', 'aa.a'))
    # print(s.match('aaa', 'ab*a'))
