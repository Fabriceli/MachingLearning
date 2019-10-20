# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-10-01 22:56
# @Author   : Fabrice LI
# @File     : 433_number_of_islands.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a boolean 2D matrix, 0 is represented as the sea,
#               1 is represented as the island. If two 1 is adjacent,
#               we consider them in the same island. We only consider up/down/left/right adjacent.
#
#               Find the number of islands.
# Reference:**********************************************
'''
E.g
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3

Input:
[
  [1,1]
]
Output:
1
'''


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid:
            return 0
        # 行
        row = len(grid)
        if not row:
            return 0
        # 列
        colum = len(grid[0])
        if not colum:
            return 0
        nums = 0
        for r in range(row):
            for c in range(colum):
                if grid[r][c]:
                    self.dfs(grid, r, c)
                    nums += 1
        return nums

    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or not grid[r][c]:
            return
        grid[r][c] = 0
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0],[1,0,1],[0,1,0]]
    print(s.numIslands(grid))
