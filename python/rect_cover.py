"""
encoding=utf-8
_author = youzipi
date = 17/11/21
"""
"""
Q:
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
"""
A:
基本结构只有两种：
1:
————
————
2：
|
|

=>
f(n) = f(n-1)+f(n-2)    # 斐波拉契数列的形式

f(1) = 1
f(2) = 2

动态规划
缩小问题规模
数学归纳法
分形
"""


class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            a = 1
            b = 2
            for i in range(number - 2):
                print(i)
                a, b = b, a + b
            return b


if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(3))
