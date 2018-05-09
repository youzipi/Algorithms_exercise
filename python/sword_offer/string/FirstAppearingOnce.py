"""
encoding=utf-8
_author = youzipi
date = 17/11/23
"""

"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""


class Solution:
    # 返回对应char
    once_word = []
    multi_times_words = {}

    def __init__(self):
        """
        for oj
        clear data
        """
        self.once_word = []
        self.multi_times_words = {}

    def FirstAppearingOnce(self):
        return len(self.once_word) and self.once_word[0] or '#'

    def Insert(self, char):
        times = self.multi_times_words.get(char)
        if times is None:
            self.once_word.append(char)
            self.multi_times_words.update({char: 1})
        else:
            self.multi_times_words.update({char: times + 1})
            if self.once_word.count(char) > 0:
                self.once_word.remove(char)


if __name__ == '__main__':
    s = Solution()
    for i in 'google':
        s.Insert(i)
        print(s.FirstAppearingOnce())

    for i in 'helloworld':
        s.Insert(i)
        print(s.FirstAppearingOnce())
