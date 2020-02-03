"""
encoding=utf-8
_author = youzipi
date = 18/7/19
"""
"""
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]



输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]


"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = nums[-k:] + nums[:(k + 1)]
        print(nums)


if __name__ == '__main__':
    s = Solution()
    result = s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    result1 = s.rotate(nums=[], k=3)
    print(result)
    print(result1)
