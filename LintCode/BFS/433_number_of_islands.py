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
import collections


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    # def numIslands(self, grid):
    #     if not grid:
    #         return 0
    #     # 行
    #     row = len(grid)
    #     if not row:
    #         return 0
    #     # 列
    #     colum = len(grid[0])
    #     if not colum:
    #         return 0
    #     nums = 0
    #     for r in range(row):
    #         for c in range(colum):
    #             if grid[r][c]:
    #                 self.dfs(grid, r, c)
    #                 nums += 1
    #     return nums
    #
    # def dfs(self, grid, r, c):
    #     if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or not grid[r][c]:
    #         return
    #     grid[r][c] = 0
    #     self.dfs(grid, r - 1, c)
    #     self.dfs(grid, r + 1, c)
    #     self.dfs(grid, r, c - 1)
    #     self.dfs(grid, r, c + 1)

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        result = 0
        visited = set()

        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if grid[c][r] == "1" and (c, r) not in visited:
                    self.bfs(grid, c, r, visited)
                    result += 1
        return result

    def bfs(self, grid, c, r, visited):
        queue = collections.deque([(c, r)])
        visited.add((c, r))
        while queue:
            x, y = queue.popleft()
            for direction_x, direction_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_x = direction_x + x
                next_y = direction_y + y
                if self.is_valid(grid, next_x, next_y, visited):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        x_edge = len(grid)
        y_edge = len(grid[0])
        if x < 0 or x >= x_edge or y < 0 or y >= y_edge:
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == "1"


if __name__ == '__main__':
    s = Solution()
    grid = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
            ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]
    print(s.numIslands(grid))
