"""
encoding=utf-8
_author = youzipi
date = 18/7/19
"""

"""
快慢指针


题目要求了 in-place 的修改，这是的方式会变得比较脏。

好久没有写C ，还有受到函数式的影响，自己已经 不适应 出参传值这种方式了。
而且大部分情况下，也不是 最佳实践。
不过在 性能有要求的情况下，如何不开辟新的内存空间 是需要考虑的问题。
这里，在满足性能的情况下，如何保证 代码的 易读， 协作，维护 呢？

"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length

        result_index = 0

        prev_val = nums[0]
        for i in range(1, length):
            if nums[i] > prev_val:
                result_index += 1
                prev_val = nums[i]
                nums[result_index] = nums[i]

        return result_index + 1


if __name__ == '__main__':
    s = Solution()
    result = s.removeDuplicates([1, 1, 2])
    print(result)
