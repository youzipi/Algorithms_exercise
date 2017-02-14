"""
encoding=utf-8
_author = youzipi
date = 16/12/9
"""

"""
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""
- 数字是乱序的
特殊情况：
- [0] :1
- [1] :0

题目要求 O(n) RC,O(1) SC
变的东西：
- 少的那个数字
- 数字的顺序
考虑不变的东西：
不管如何输入,nums的父集合是不变的，对于该父集合，内部所有数字的和是不变的

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = len(nums) * (len(nums) + 1) / 2
        for i in nums:
            sum -= i
        return sum


s = Solution()
result = s.missingNumber([0, 4, 3, 2])
print(result)
