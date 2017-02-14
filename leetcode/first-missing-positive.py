"""
encoding=utf-8
_author = youzipi
date = 16/12/9
"""

"""
https://leetcode.com/problems/first-missing-positive/

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 2
        num_set = {}
        for num in nums:
            num_set[num] = 1
        for index, val in num_set.items():
            if index == 0:
                continue
            if val == 0:
                return index


s = Solution()
result = s.firstMissingPositive([2])
print(result)
