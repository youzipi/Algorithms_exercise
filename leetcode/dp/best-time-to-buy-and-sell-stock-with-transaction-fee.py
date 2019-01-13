"""
encoding=utf-8
_author = youzipi
date = 2019/1/13
"""
"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

"""

"""
dp[i][0] = max(
            dp[i][0],
            dp[i][1] + p[i],
            )
dp[i][1] = max(
            dp[i][1],
            dp[i][0] - p[i] - fee,
            ) 


## 手续费 是在买入时计算，还是在 卖出时计算？

最大的收益肯定是 最后 不持有股票，所以在哪儿算都是一样的。

"""


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0

        r = [[0, 0] for i in range(0, length)]

        r[0][1] = -prices[0] - fee

        for i in range(1, length):
            r[i][0] = max(
                r[i - 1][0],
                r[i - 1][1] + prices[i],
            )

            r[i][1] = max(
                r[i - 1][1],
                r[i - 1][0] - prices[i] - fee,
            )
        return r[length - 1][0]


if __name__ == '__main__':
    s = Solution()
    # result = s.maxProfit([1, 2, 3, 0, 2])
    result = s.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2)
    print(result)
