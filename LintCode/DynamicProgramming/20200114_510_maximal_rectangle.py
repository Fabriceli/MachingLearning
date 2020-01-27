# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-15 01:11
# @Author   : Fabrice LI
# @File     : 20200114_510_maximal_rectangle.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a 2D boolean matrix filled with False and True,
#               find the largest rectangle containing all True and return its area.
#Reference:**********************************************
"""
Input:
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
Output: 6

Input:
[
    [0,0],
    [0,0]
]
Output: 0
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows = len(matrix)
        columns = len(matrix[0])

        dp = [[0 for _ in range(columns)] for _ in range(rows)]

        for r in range(rows):

            for c in range(columns):
                if matrix[r][c] == 1:
                    pass
