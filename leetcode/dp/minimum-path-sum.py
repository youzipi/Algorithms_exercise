"""
encoding=utf-8
_author = youzipi
date = 2019/1/13
"""

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

"""
dp[i][j] 
从 (0,0) 到 (i,j) 的 最小路径和

dp[i][j] = min(
            dp[i][j-1] + p[i][j],
            dp[i-1][j] + p[i][j],
        )

"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0

        h_length = len(grid)
        v_length = len(grid[0])

        # r = [[0 for j in range(v_length)] for i in range(h_length)]
        r = [[0] * v_length] * h_length

        r[0][0] = grid[0][0]

        for i in range(1, h_length):
            r[i][0] = r[i - 1][0] + grid[i][0]

        for j in range(1, v_length):
            r[0][j] = r[0][j - 1] + grid[0][j]

        for i in range(1, h_length):
            for j in range(1, v_length):
                r[i][j] = min(
                    r[i][j - 1] + grid[i][j],
                    r[i - 1][j] + grid[i][j],
                )
        return r[h_length - 1][v_length - 1]


if __name__ == '__main__':
    s = Solution()
    r = s.minPathSum(grid=
    # [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    [
        [0, 1],
        [1, 0],
    ]
    )
    print(r)
