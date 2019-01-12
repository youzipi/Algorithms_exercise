"""
encoding=utf-8
_author = youzipi
date = 17/11/23
"""
"""
title = 数组中重复的数字

题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        l = [0] * len(numbers)
        for i in numbers:
            if l[i] > 0:
                duplication[0] = i
                return True
            l[i] += 1
        return False


if __name__ == '__main__':
    s = Solution()
    a = [-1]
    # result = s.duplicate([2, 1, 3, 1, 4], a)
    result = s.duplicate([2, 3, 1, 0, 2, 5, 3], a)
    print(result)
    print(a[0])
