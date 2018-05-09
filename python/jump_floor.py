"""
encoding=utf-8
_author = youzipi
date = 17/11/21
"""

"""
Q:
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
"""

A:
先走一步，看看。
从具体出发，假设n=3,画出所有方案的树状图。
第几层代表第几步，顶层=0。

f(n) =  f(n-1) # 第一步=1
        + f(n-2)    # 第一步=2
        
f(1) = 1
f(2) = 2


"""


class Solution:
    def jumpFloor1(self, number):
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)

    def jumpFloor(self, number):
        def _jump(number, a, b):
            if number == 1:
                return 1
            elif number == 2:
                return 2
            else:
                return _jump(number - 1, b, a + b)

        return _jump(number, 0, 1)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(3))
