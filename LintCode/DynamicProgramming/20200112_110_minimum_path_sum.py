# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-12 11:27
# @Author   : Fabrice LI
# @File     : 20200112_110_minimum_path_sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a m x n grid filled with non-negative numbers, find a path from top left to
#               bottom right which minimizes the sum of all numbers along its path.
#Reference:**********************************************
"""
Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7

	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1

Input:  [[1,3,2]]
	Output: 6

	Explanation:
	Path is: 1 -> 3 -> 2
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        column = len(grid[0])
        dp = [[0 for _ in range(column)] for _ in range(2)]
        dp[0][0] = grid[0][0]

        for r in range(row):
            for c in range(column):
                if r == 0 and c > 0:
                    dp[r%2][c] = grid[r][c] + dp[r%2][c - 1]
                elif r > 0 and c == 0:
                    dp[r%2][c] = grid[r][c] + dp[(r - 1)%2][c]
                elif r > 0 and c > 0:
                    dp[r%2][c] = min(dp[(r - 1)%2][c], dp[r%2][c - 1]) + grid[r][c]
        print(dp)
        return dp[(row + 1)%2][-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        column = len(grid[0])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        dp[0][0] = grid[0][0]

        for r in range(row):
            for c in range(column):
                if r == 0 and c > 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1]
                elif r > 0 and c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c]
                elif r > 0 and c > 0:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
        print(dp)
        return dp[row - 1][-1]


if __name__ == '__main__':
    s = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minPathSum(grid))
