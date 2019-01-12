"""
encoding=utf-8
_author = youzipi
date = 2019/1/9
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            r_low = 1
            r_high = 2
        for i in range(2, n):
            r_low, r_high = r_high, r_high + r_low

        return r_high


if __name__ == '__main__':
    s = Solution()
    result = s.climbStairs(38)
    print(result)
