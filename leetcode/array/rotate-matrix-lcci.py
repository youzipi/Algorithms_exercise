
from typing import List

"""
https://leetcode-cn.com/problems/rotate-matrix-lcci/
矩阵 旋转 90度


Given an image represented by an N x N matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. 
Can you do this in place?

 

Example 1:

Given matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

Rotate the matrix in place. It becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


方案1：
找出 第 i 圈，观察 4个角移动的特点和关系。

方案2：
矩阵 沿 左上-右下 对角反转
再沿 左右翻转

"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for level in range(0, n - 1):
            """
            第 i 层，从 i,i -> i,n-1-i -> n-1-i,n-1-i -> n-1-i,i
            左上 每向右移动一
            -> 右上 向下移动一
            -> 右下 向左 移动一
            -> 左下 向上 移动一
            """
            for j in range(level, (n - 1 - level)):
                x1 = level
                y1 = j
                x2 = j
                y2 = n - 1 - level
                x3 = n - 1 - level
                y3 = n - 1 - j
                x4 = n - 1 - j
                y4 = level

                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4], = matrix[x4][y4], matrix[x1][y1], \
                                                                                  matrix[x2][y2], matrix[x3][y3],
