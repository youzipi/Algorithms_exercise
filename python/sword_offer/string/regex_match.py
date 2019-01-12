"""
encoding=utf-8
_author = youzipi
date = 18/5/30
"""
"""
3.3 
ex 19

title = 正则表达式 匹配 
desc = 

请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

"""


class Token:
    ch = ''
    type = ''

    def __init__(self, ch, type):
        self.ch = ch
        self.type = type

    def __repr__(self):
        return str(self.__dict__)


class Group:
    tokens = []

    def __init__(self):
        self.tokens = []

    def add_token(self, ch='', type=''):
        if ch == '':
            return False
        else:
            token = Token(ch=ch, type=type)
            # print('token=', token)
            self.tokens.append(token)
            return True

    def __repr__(self):
        return str(self.__dict__)


class Solution:

    # s, pattern都是字符串
    def match(self, s, pattern):
        chars = list(s)
        length = len(chars)

        lookup = ''
        group = Group()

        pattern_length = len(pattern)
        if length == 0 and pattern_length == 0:
            return True
        # elif length == 0 and pattern_length > 0:
        #     return False
        elif length > 0 and pattern_length == 0:
            return False

        for p in pattern:
            if p == '.':
                group.add_token(ch=lookup,
                                type='')
                lookup = p

            elif p == '*':
                group.add_token(ch=lookup,
                                type=p)
                lookup = ''
            else:
                group.add_token(ch=lookup,
                                type='')
                lookup = p
        group.add_token(ch=lookup,
                        type='')

        print(group)

        max_index = length - 1
        i = 0
        ch = ''
        type = ''
        for token in group.tokens:
            ch = token.ch
            type = token.type
            if ch == '.' and type == '*':
                return length == 0

            if ch == '.':
                ch = chars.__getitem__(i)
                i += 1
                if i > max_index:
                    return False

            if type == '*':
                while chars.__getitem__(i) == ch:
                    i += 1
                    if i > max_index:
                        return False
            else:
                if chars.__getitem__(i) == ch:
                    i += 1
                    if i > max_index:
                        return False
                else:
                    return False

        return i == max_index or (i == 0 and length == 0)


# write code here


if __name__ == '__main__':
    s = Solution()

    # t = Token(ch='123', type='123')
    # print(t)

    # print(s.match('aaa', 'a.a'))
    # print(s.match('aaa', 'aa.a'))
    # print(s.match('aaa', 'ab*a'))
    # print(s.match('', ''))
    # print(s.match('a', ''))
    print(s.match("", "."))
    # print(s.match("", ".*"))
