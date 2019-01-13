"""
encoding=utf-8
_author = youzipi
date = 2019/1/12
"""
"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""

"""
i = 0 -> length-1
j = 0 -> 1  # 持有股数
f = 0 -> 1  # isFrozen

前一天 的 状态有 4 种：
dp[i-1][0][0] # 可买入
dp[i-1][0][1] # frozen
dp[i-1][1][0] # 可卖出

很像一个状态机
            
dp[i][0][0] = max( 
            dp[i-1][0][0],
            dp[i-1][0][1],
            # dp[i-1][1][0],
            )
dp[i][0][1] = max( 
            # dp[i-1][0][0],
            # dp[i-1][0][1],
            dp[i-1][1][0] + p[i]
            )
dp[i][1][0] = max( 
            dp[i-1][0][0] - p[i],
            # dp[i-1][0][1],
            dp[i-1][1][0],
            )

    

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        if length <= 1:
            return 0

        # init
        r = [[[0 for h in (0, 1)] for j in (0, 1)] for i in range(length)]

        r[0][0][0] = 0
        r[0][0][1] = False
        r[0][1][0] = -prices[0]

        def safe(r, i, j, h):
            if i >= len(r) or j >= len(r[i]) or h >= len(r[i][j]):
                return False
            elif i < 0 or j < 0 or h < 0:
                return False
            elif r[i][j][h] is False:
                return False
            else:
                return True

        for i in range(1, length):

            r_list = []
            if safe(r, i - 1, 1, 0):
                r_list.append(r[i - 1][0][0])
            if safe(r, i - 1, 1, 1):
                r_list.append(r[i - 1][0][1])
            if len(r_list) == 0:
                r[i][0][0] = False
            else:
                r[i][0][0] = max(r_list)

            r[i][0][1] = r[i - 1][1][0] + prices[i]

            r_list = []
            if safe(r, i - 1, 0, 0):
                r_list.append(r[i - 1][0][0] - prices[i])
            if safe(r, i - 1, 1, 0):
                r_list.append(r[i - 1][1][0])
            if len(r_list) == 0:
                r[i][1][0] = False
            else:
                r[i][1][0] = max(r_list)

        for i in r:
            print(i)
        return max(r[length - 1][0])


if __name__ == '__main__':
    s = Solution()
    # result = s.maxProfit([1, 2, 3, 0, 2])
    result = s.maxProfit([3, 3])
    print(result)
