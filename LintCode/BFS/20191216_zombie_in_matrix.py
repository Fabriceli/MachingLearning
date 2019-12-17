# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-16 18:14
# @Author   : Fabrice LI
# @File     : 20191216_zombie_in_matrix.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
#               Zombies can turn the nearest people(up/down/left/right) into zombies every day,
#               but can not through wall. How long will it take to turn all people into zombies?
#               Return -1 if can not turn all people into zombies.
#Reference:**********************************************
"""
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2

Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4
"""
import collections

PEOPLE = 0
ZOMBIE = 1
WALL = 2


class Solution:
    def zombie(self, grid):
        if not grid or not grid[0]:
            return 0
        queue = collections.deque()
        row = len(grid)
        column = len(grid[0])

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1:
                    queue.append((r, c))
        result = 0

        while queue:
            size = len(queue)
            result += 1
            for _ in range(size):
                x, y = queue.popleft()
                for delta_x, delta_y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    next_x = delta_x + x
                    next_y = delta_y + y
                    if next_x < 0 or next_x >= row or next_y < 0 or next_y >= column:
                        continue
                    if grid[next_x][next_y] == ZOMBIE or grid[next_x][next_y] == WALL:
                        continue
                    grid[next_x][next_y] = ZOMBIE
                    queue.append((next_x, next_y))
        for g in grid:
            if PEOPLE in g:
                return -1
        return result - 1


if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,2,0,0],
            [1,0,0,2,1],
            [0,1,0,0,0]]
    grid1 = [[0,0,0],
             [0,0,0],
             [0,0,1]]
    print(s.zombie(grid1))
