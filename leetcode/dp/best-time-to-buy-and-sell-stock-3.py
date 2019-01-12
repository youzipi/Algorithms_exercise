"""
encoding=utf-8
_author = youzipi
date = 2019/1/10
"""
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1] 
输出: 0 
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

"""

"""
最大的两次收益保存起来
max_profit[2]


=>
找出 所有的递增子序列

把 这个子序列集合中，增长最多的结果保存下来。

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

        p_max = 0
        p_max_second = 0
        # 本次递增序列 收益记录
        profit = 0
        for i in range(1, length):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
            else:
                if profit > p_max:
                    p_max, p_max_second = profit, p_max
                elif profit > p_max_second:
                    p_max_second = profit
                profit = 0
                # print(p_max, p_max_second)
            # print(profit)
        if profit > p_max:
            p_max, p_max_second = profit, p_max
        elif profit > p_max_second:
            p_max_second = profit

        return p_max + p_max_second


if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])
    # result = s.maxProfit([7,6,4,3,1])
    print(result)
