"""
encoding=utf-8
_author = youzipi
date = 2019/1/13
"""

"""
index = 300

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18,20]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,18,20]，它的长度是 5。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

"""

"""
维护 上升子序列

当出现比 当前 LIS 的 最大值 小 的值 的话，替换掉。
长度不变，你

"""

"""

dp[i]
定义：以 第 i 个 元素结尾 的 最长子序列的长度

result = max(dp[0],dp[1],...dp[n-1])


dp[i] = max{dp[j]} + 1 
j 满足：
- j < i
- p[j] < p[i]
"""

"""
状态是 复合的，
包含：
最大长度，
前一个最大值

dp[i] = (max_length, last_val)


dp[i] = (
        p[i]>dp[i-1].last_val
        ? (
            dp[i-1].max_length + 1,
            p[i],
            ) 
        : dp[i-1]
        )

但是从例中看出，那个 5 没有加入，虽然 5 加入的话，最后的结果是一样的，但如果是 [2, 5, 3, 4, 101] 的话，5 加入就会影响，
所以 如果 p[i]>dp[i-1].last_val 的话，也要把 加入|不加入 两种情况 保存下来。

i-1_max = dp[i-1][1].max_length > dp[i-1][0].max_length 
            ? dp[i-1][1]
            : dp[i-1][0]
            
dp[i][0] = i-1_max

dp[i][1] = (
        p[i]>dp[i-1].last_val
        ? (
            dp[i-1].max_length + 1,
            p[i],
            ) 
        : False
        )

"""


class Result:
    def __init__(self, length=0, last_val=0) -> None:
        self.length = length
        self.last_val = last_val


class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length

        r = [1 for i in range(0, length)]

        for i in range(1, length):
            max_length = 1
            i_val = nums[i]
            for j in range(0, i):
                if nums[j] < i_val:
                    max_length = max(max_length, r[j] + 1)
            r[i] = max_length
        print(r)
        return max(r)


if __name__ == '__main__':
    s = Solution()
    # result = s.maxProfit([1, 2, 3, 0, 2])
    result = s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 20])
    # result = s.lengthOfLIS([-2, -1])
    print(result)
