# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-11 22:48
# @Author   : Fabrice LI
# @File     : 20200111_436_maximal_square.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a 2D binary matrix filled with 0's and 1's,
#               find the largest square containing all 1's and return its area.
#Reference:**********************************************
"""
Input:
[
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
Output: 4

Input:
[
  [0, 0, 0],
  [1, 1, 1]
]
Output: 1
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        dp = [[0 for _ in range(column)] for _ in range(2)]
        ans = 0

        for r in range(row):
            for c in range(column):
                if r == 0 or c == 0:
                    dp[r % 2][c] = int(matrix[r][c])
                else:
                    if matrix[r][c] == '1':
                        dp[r % 2][c] = min(dp[(r - 1) % 2][c - 1], dp[(r - 1) % 2][c], dp[r % 2][c - 1]) + 1
                    else:
                        dp[r % 2][c] = 0
                ans = max(dp[r % 2][c], ans)

        return ans * ans


if __name__ == '__main__':
    s = Solution()
    matrix = [
  ['0', '0', '0'],
  ['1', '1', '1']
]
    print(s.maximalSquare(matrix))

