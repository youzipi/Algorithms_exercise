"""
encoding=utf-8
_author = youzipi
date = 18/5/9
"""
"""
问题描述
假设我们有一个数组， 数组中按顺序每个元素的值表示当天的股票价格。
例如，数组： [7,1,5] 表示股票第一天是7元，第二天是1元，第三天是5元 约定，只能买一次，卖一次，而且必须是先买后卖。 

设计一个算法，找到第几次买和第几次卖，能够实现最大利润。

举例：

输入: [7,1,5,3,6,4]
输出: 5
注解: 第2天买，第5天卖，最大利润是（6-1）：5
不是7-1=6, 因为只能先买后卖。

输入: [7,6,4,3,1]
输出: 0
注解: 不能先买后卖，所以利润为0.

链接：https://www.imooc.com/article/28425

#S
绘制成 折线图
实质是 求 最低点 和 最高点 的差值，
同时最低点 早于 最高点(T+1)

> 对于数组问题，不妨使用图表法，从图表中，找到问题的本质。




一个点 从前往后 移动
两个值 分别表示 当前最小值 和 最大差值

用 当前值-当前最小值 和 最大差值 比较
（这里隐含的一个因素是：当前值的时间 一定 晚于 当前最小值的时间）

#S2
存在 最优子结构


"""


class Solution:

    def max_profit(self, arr=None):
        if arr is None:
            arr = []
        if len(arr) == 0:
            return 0, 0, 0,
        else:
            min_val = arr[0]
            min_index = 0

            max_profit = arr[1] - arr[0]
            buy_index = 0
            sell_index = 1
            length = len(arr)

            for i in range(length):
                v = arr[i]
                if v < min_val:
                    min_val = v
                    min_index = i
                elif (v - min_val) > max_profit:
                    buy_index = min_index
                    sell_index = i
                    max_profit = v - min_val

            if max_profit <= 0:
                return 0, 0, 0
            else:
                return buy_index, sell_index, max_profit


if __name__ == '__main__':
    s = Solution()
    result = s.max_profit(arr=[7, 1, 5, 3, 6, 4])
    print(result)

    print(s.max_profit(arr=[7, 6, 4, 3, 1, ]))
    print(s.max_profit(arr=[7, 2, 5, 3, 6, 4, 1, 7]))
