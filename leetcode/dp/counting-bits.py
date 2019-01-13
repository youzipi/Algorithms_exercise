"""
encoding=utf-8
_author = youzipi
date = 2019/1/13
"""

"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
"""

"""
me:

列出了 0 -> 16 ，以及 1 的个数，以及 相对前一个的变化。
发现了规律：
首先，如果 i 为 奇数的话， dp[i] = dp[i-1] + 1

而偶数的话，对于 2 的 x 次幂，dp[i] 都是 1
dp[16] = dp[8] = dp[4] = ... = dp[1] = 1

推而广之，所有的偶数，因为 个位 都是 0，所以 1 的 个数，和 降了一维 的结果一样，也就是 i/2 的 1 的个数。

如果 i 为 偶数的话， dp[i] = dp[i/2]

"""


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = [0 for i in range(num + 1)]

        for i in range(1, num + 1):
            if (i % 2) == 0:
                r[i] = r[int(i / 2)]
            else:
                r[i] = r[i - 1] + 1
        return r


if __name__ == '__main__':
    s = Solution()
    result = s.countBits(5)
    print(result)
