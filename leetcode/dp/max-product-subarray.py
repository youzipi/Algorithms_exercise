"""
encoding=utf-8
_author = youzipi
date = 2019/1/9
"""
"""
保存 最大值 和 最小值

最小值 通常是 负数。

画一个直角坐标系，最小值 和 最大值 是 偏离 x 轴 最远 的两个。




dp[i] = dp[i-1]*a[i]

(i_max,i_min) = ( (i-1_max,i-1_min), t[i] )


    dp[i, max] = ( a[i] > 0 ) ? dp[i-1, max] * a[i] : dp[i-1,min] * a[i]
    dp[i, min] = ( a[i] > 0 ) ? dp[i-1, min] * a[i] : dp[i-1,max] * a[i]


other:
判断 序列中是否 包含 0：
如果有 0 的话，两边其实是连不上的。
所以在 0 的两边，分别求 最大值，循环调用 maxProduct。
序列特别长的话，这样的分治 可以 提升效率。


"""


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_list = [0] * length
        min_list = [0] * length

        max_list[0] = min_list[0] = nums[0]
        for i in range(1, length):
            value = nums[i]
            max_list[i] = max(max_list[i - 1] * value, min_list[i - 1] * value, value)
            min_list[i] = min(min_list[i - 1] * value, max_list[i - 1] * value, value)

        print(max_list, min_list)
        return max(max_list)


if __name__ == '__main__':
    s = Solution()
    result = s.maxProduct([-2, 3, -4])
    print(result)
