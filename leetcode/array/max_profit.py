"""
encoding=utf-8
_author = youzipi
date = 18/7/19
"""
"""
算出 每天 相对于前一天的 价格变化

[7, 1, 5, 3, 6, 4]
得到：
[0, -6, 4, -2, 3, -2]

[1, 2, 3, 4, 5]:
得到:
[0, 1, 1, 1, 1]

这样就变成了 寻找 数组中 非负 序列和

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        prev_price = 0
        change_l = []
        for i in prices:
            change_l.append(i - prev_price)
            prev_price = i

        change_l[0] = 0
        print(change_l)
        profit = 0
        for i in range(len(change_l)):
            change = change_l[i]
            if change >= 0:
                profit += change
        return profit


if __name__ == '__main__':
    s = Solution()
    result = s.maxProfit([7, 1, 5, 3, 6, 4])
    result1 = s.maxProfit([1, 2, 3, 4, 5])
    result2 = s.maxProfit([7, 6, 4, 3, 1])
    result3 = s.maxProfit([])

    print(result)
    print(result1)
    print(result2)
    print(result3)
