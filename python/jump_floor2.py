"""
encoding=utf-8
_author = youzipi
date = 17/11/21
"""

"""
Q:
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
"""

A:
先走一步，看看。
从具体出发，假设n=3,画出所有方案的树状图。
第几层代表第几步，顶层=0。

f(n) =  f1(n,n) 
    = 1 + sum( f1(n-i,n-i) )
n = 3:
f(3,3) = 1        # 第一步=3
    + f1(1,1)   # 第一步=2
    + f1(2,2)   # 第一步=1
    
f1(2,2) = 1 # 第一步=2
    + f1(1,1)   # 第一步=1
    
f1(1,1) = 1 # 第一步=1

=> f(3) = 4

f1(总台阶数，每步最大台阶数):
    pass
    
https://www.nowcoder.com/questionTerminal/22243d016f6b47f2a6928b4313c85387    
牛客 还给出了其他解法：
每个台阶都有跳与不跳两种情况（除了最后一个台阶），最后一个台阶必须跳。所以共用2^(n-1)中情况

"""


class Solution:
    def jump(self, number, max_step):
        if number == 0:
            return 0
        else:
            sum = 1
            for i in range(number):
                sum += self.jump(i, i)
            return sum

    def jumpFloorII(self, number):
        return self.jump(number, number)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(3))
