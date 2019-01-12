"""
encoding=utf-8
_author = youzipi
date = 2019/1/10
"""
import random

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3。
"""

"""
最大的两次收益保存起来
max_profit[2]


=>

todo
找出 所有的递增子序列，分 区间 处理


"""


class Solution:
    def maxProfitNoBuyLimit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        无限次买卖
        
        todo 无限次买卖，但限制最大持股数
        """
        length = len(prices)
        if length <= 1:
            return 0

        profit = 0
        for i in range(1, length):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff

        return profit

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        """
        第几天：i = 0 -> length-1
        已购买次数： j = 0 -> k
        持有股数： h = 0 -> max_hold
        
        隐含条件： 
        - max_hold <= k <= length
        - h <= j <= i
        相等的情况是，每天都买，只买不卖，此时 h = j = i
        
        推导出条件
        - j <= min(i,k)
        - h <= min(j,max_hold)
        
        条件外的情况不会发生，不需要考虑
        
        r 表示的是状态，即 第 i 天，购买 j 次，持有 h 股的情况下，最大的收益
        考虑下 第 0 天，j 和 h 都 只能为 0 
        
        """
        length = len(prices)
        if length <= 1 or k <= 0:
            return 0
        elif k > length:
            # 最多交易次数 大于 天数，则 退化为 贪心算法
            return self.maxProfitNoBuyLimit(prices)

        max_hold = 1
        _k = min(k, length)
        _max_hold = min(max_hold, k)

        print(length, _k, _max_hold)

        # r 标识
        # r = [[[0 for h in range(max_hold + 1)] for j in range(k + 1)] for i in range(length)]
        # r = [[[0 for h in range(_max_hold + 1)] for j in range(_k + 1)] for i in range(length)]
        r = [[[0 for h in range(min(j, _max_hold) + 1)] for j in range(min(i + 1, _k) + 1)] for i in range(length)]

        # 初始化第一天数据
        r[0][1][1] = -prices[0]

        for i in r:
            print(i)

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
            # 第 i 天，购买次数 j <= min(i,k)
            j_max = min(i + 1, _k)
            for j in range(j_max + 1):
                # 购买 j 次 的情况下， h <= min(j,max_hold)
                h_max = min(j, _max_hold)
                for h in range(h_max + 1):
                    print(i, j, h)

                    # 参与比较 的 r
                    r_list = []

                    # 如果 来源节点 不存在的话，不应该 返回一个 默认值，应该不参与比较
                    if safe(r, i - 1, j, h):
                        r_list.append(r[i - 1][j][h])
                    if safe(r, i - 1, j - 1, h - 1):
                        # 只有 买入的时候，j 才 增加 1，以 购买次数 作为交易次数
                        r_list.append(r[i - 1][j - 1][h - 1] - prices[i])
                    if safe(r, i - 1, j, h + 1):
                        r_list.append(r[i - 1][j][h + 1] + prices[i])

                    if len(r_list) == 0:
                        r[i][j][h] = False
                    else:
                        r[i][j][h] = max(r_list)

                    # r[i][j][h] = max(
                    #     # r[i - 1][j][h],  # hold
                    #     # r[i - 1][j - 1][h - 1] - prices[i],  # buy
                    #     # r[i - 1][j - 1][h + 1] + prices[i],  # sell
                    #     safe(r, i - 1, j, h) and r[i - 1][j][h] or 0,  # hold
                    #     safe(r, i - 1, j - 1, h - 1) and (r[i - 1][j - 1][h - 1] - prices[i]) or 0,  # buy
                    #     safe(r, i - 1, j - 1, h + 1) and (r[i - 1][j - 1][h + 1] + prices[i]) or 0,  # sell
                    # )
        for i in r:
            print(i)
        return max((max(max(r[i][j]) for j in range(min(i + 1, _k) + 1)) for i in range(length)))


if __name__ == '__main__':
    s = Solution()
    # result = s.maxProfit(2, [3, 2, 6, 5, 0, 3])
    # result = s.maxProfit(2, [2, 4, 1])
    # result = s.maxProfit(0, [1, 3])
    prices = [random.randint(0, 1000) for i in range(10000)]
    # result = s.maxProfit(2, [1, 2, 4])
    result = s.maxProfit(1000000000, prices)
    # result = s.maxProfit([7,6,4,3,1])
    print(result)
