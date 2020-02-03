"""
encoding=utf-8
_author = youzipi
date = 2019/1/15
"""

"""
index = 72

编辑距离
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
"""

"""
经验：字符串匹配类型的题目，
dp[i][j]
定义为 word1 的 前 i 个字符 转换为 word2 的 前 j 个字符，最少需要的步数。

尝试推导：
先从 特殊情况考虑：
word1 = '',word2 = ''
此时，需要 0步。

word1 = '',word2 = 'ss'
此时，需要 2 步。（word1 增加2次）

word1 = 'ss', word2 = ''
此时，需要 2 步。（word1 删除 2次）

word1 = 'ss', word2 = 'ssr'
此时，需要 1 步。（word1 增加 1 次）

word1 = 'ss', word2 = 'st'
此时，需要 1 步。（word1 替换 1 次）

再考虑一般情况：

len1 = len(word1)
len2 = len(word2)

word1 到 word2 的距离
为
word1 - word1[-1],
word2 - word2[-1] 
这两个字符串 的距离 
加上 word1[-1], word2[-1] 的距离。
word1[-1] 到 word2[-1] 
可能为 0 # 这两个字符相等。
可能为 1 # replace | insert | delete



"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
