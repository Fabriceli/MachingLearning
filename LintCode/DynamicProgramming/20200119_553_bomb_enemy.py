# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-19 11:30
# @Author   : Fabrice LI
# @File     : 20200119_553_bomb_enemy.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
#               return the maximum enemies you can kill using one bomb.
#               The bomb kills all the enemies in the same row and column from the planted point until
#               it hits the wall since the wall is too strong to be destroyed.
#Reference:**********************************************
"""
You can only put the bomb at an empty cell.

Input:
grid =[
     "0E00",
     "E0WE",
     "0E00"
]
Output: 3
Explanation:
Placing a bomb at (1,1) kills 3 enemies

Input:
grid =[
     "0E00",
     "EEWE",
     "0E00"
]
Output: 2
Explanation:
Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies
"""
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        columns = len(grid[0])
        up = [[0 for _ in range(columns)] for _ in range(rows)]
        down = [[0 for _ in range(columns)] for _ in range(rows)]
        right = [[0 for _ in range(columns)] for _ in range(rows)]
        left = [[0 for _ in range(columns)] for _ in range(rows)]
        # 计算up方向
        for r in range(rows):
            for c in range(columns):
                # 先看是不是墙，是墙的话直接下一步
                if grid[r][c] == 'W':
                    up[r][c] = 0
                    continue
                up[r][c] = 1 if grid[r][c] == 'E' else 0
                if r > 0:
                    up[r][c] += up[r - 1][c]
        # 计算down方向
        for r in range(rows - 1, -1, -1):
            for c in range(columns):
                # 先看是不是墙，是墙的话直接下一步
                if grid[r][c] == 'W':
                    down[r][c] = 0
                    continue
                down[r][c] = 1 if grid[r][c] == 'E' else 0
                if r < rows - 1:
                    down[r][c] += down[r + 1][c]

        # 计算right方向
        for r in range(rows):
            for c in range(columns):
                # 先看是不是墙，是墙的话直接下一步
                if grid[r][c] == 'W':
                    right[r][c] = 0
                    continue
                right[r][c] = 1 if grid[r][c] == 'E' else 0
                if c > 0:
                    right[r][c] += right[r][c - 1]

        # 计算left方向
        for r in range(rows):
            for c in range(columns - 1, -1, -1):
                # 先看是不是墙，是墙的话直接下一步
                if grid[r][c] == 'W':
                    left[r][c] = 0
                    continue
                left[r][c] = 1 if grid[r][c] == 'E' else 0
                if c < columns - 1:
                    left[r][c] += left[r][c + 1]

        # 汇总统计结果
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '0':
                    res = max(res, up[r][c] + down[r][c] + left[r][c] + right[r][c])
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
    print(s.maxKilledEnemies(grid))
