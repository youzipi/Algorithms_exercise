"""
encoding=utf-8
_author = youzipi
date = 17/11/23
"""
"""
title = 二维数组中的查找

题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""
A:

>
* 矩阵是有序的，从左下角来看，向上数字递减，向右数字递增，
* 因此从左下角开始查找，当要查找数字比左下角数字大时。右移
* 要查找数字比左下角数字小时，上移

寻找有序路径
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row_limit = len(array) - 1
        column_limit = len(array[0]) - 1
        i = j = 0
        while i < row_limit:
            print(i, j)
            a = array[i][j]
            if a > target:
                i -= 1
                j += 1
                break
            elif a == target:
                return True
            i += 1
        while j <= column_limit and i >= 0:
            print(i, j)
            a = array[i][j]
            if a > target:
                i -= 1
            if a < target:
                j += 1
            elif a == target:
                return True
        return False


if __name__ == '__main__':
    s = Solution()

    result = s.Find(15, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])

    print(result)
