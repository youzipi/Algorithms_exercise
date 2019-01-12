"""
encoding=utf-8
_author = youzipi
date = 2019/1/9
"""
"""
t[i,j] = t[i+1, j] + t[i+1,j+1]

[0,0]
[1,0],[1,1]
[2,0],[2,1],[2,2]

共 x 层，第 i 层 有 i 个 元素

r[i] = min( min_list(i) )


本题中的状态是个 tuple
（当前行每个节点的最短路径，上一行数据） = （下一行每个节点的最短路径，当前行数据）
f(min_list(i),t[i+1])
= f(min_list(i-1),t[i])


本题中，
全局最优 无法从 前一行的 局部最优 得到，
而是从 前一行的 局部最优的集合 得到。 

"""


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        high_list = []
        low_list = []
        total_level = len(triangle)

        # (total_level - 1) => 0
        for cur_level in range(total_level - 1, -1, -1):
            if cur_level == (total_level - 1):
                high_list = triangle[cur_level]
            else:
                total_index = cur_level + 1
                low_list = high_list
                high_list = [0] * total_index
                # 0 => (total_index - 1)
                for cur_index in range(0, total_index):
                    cur_node = triangle[cur_level][cur_index]
                    high_list[cur_index] = cur_node + min(low_list[cur_index], low_list[cur_index + 1])
                    # high_list.append(cur_node + min(low_list[cur_index], low_list[cur_index + 1]))
            print(high_list)

        return high_list[0]


if __name__ == '__main__':
    s = Solution()
    t = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
    result = s.minimumTotal(t)
    print(result)
