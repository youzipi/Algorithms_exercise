"""
encoding=utf-8
_author = youzipi
date = 18/5/30
"""
"""
title = 表示数值的字符串

desc = 
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        pass


if __name__ == '__main__':
    s = Solution()
    s.isNumeric("+100")
    s.isNumeric("5e2")
    s.isNumeric("-123")
    s.isNumeric("3.1416")
    s.isNumeric("-1E-16")
    #
    s.isNumeric("12e")
    s.isNumeric("1a3.14")
    s.isNumeric("1.2.3")
    s.isNumeric("+-5")
    s.isNumeric("12e+4.3")
