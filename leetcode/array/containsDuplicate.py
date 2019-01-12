"""
encoding=utf-8
_author = youzipi
date = 18/7/20
"""

"""
 存在重复
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniques = {}
        for i in nums:
            if uniques.get(i) is None:
                uniques.update({i: 1})
            else:
                return True
        return False

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    s = Solution()
    result = s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    result1 = s.containsDuplicate1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(result)
    print(result1)
