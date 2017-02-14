"""
encoding=utf-8
_author = youzipi
date = 16/12/9
"""
"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

"""

"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_list = [0 for i in range(n)]
        for num in nums:
            num_list[num] += 1
        for index, val in enumerate(num_list):
            if val > 1:
                return index


s = Solution()
result = s.findDuplicate([0, 1, 2, 3, 4, 3])
print(result)
