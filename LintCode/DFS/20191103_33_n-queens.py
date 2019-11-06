# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-11-03 12:01
# @Author   : Fabrice LI
# @File     : 20191103_33_n-queens.py
# @User     : liyihao
# @Software : PyCharm
# @Description: The n-queens puzzle is the problem of placing n queens on an n×n chessboard
#               such that no two queens attack each other(Any two queens can't be in the same row,
#               column, diagonal line).
#
#               Given an integer n, return all distinct solutions to the n-queens puzzle.
#
#               Each solution contains a distinct board configuration of the n-queens' placement,
#               where 'Q' and '.' each indicate a queen and an empty space respectively.
# Reference:**********************************************
'''
E.g
Input:1
Output:
   [["Q"]]

Input:4
Output:
[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]

Challenge
Can you do it without recursion?
'''
from typing import List


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        if n <= 0:
            return []
        res = []
        queens = [[0 for _ in range(n)] for _ in range(n)]
        self.dfs(n, 0, queens, res)
        return res

    def dfs(self, n, cur_row, queens, res):
        if cur_row == n:
            print(queens)
            return
        for column in range(n):
            if self.is_valide(cur_row, column, queens):
                queens[cur_row][column] = 1
                self.dfs(n, cur_row + 1, queens, res)
                queens[cur_row][column] = 0

    def set_str(self, string, i, s):
        t = list(string)
        t[i] = s
        return ''.join(t)

    def is_valide(self, cur_row, column, queens):
        # 行里面有Q，返回False
        # for c in range(column):
        #     if queens[cur_row][c] == 'Q':
        #         return False
        # if queens[cur_row][:column].count('Q'):
        #     return False
        # 列里面有Q，返回False
        for r in range(cur_row):
            if queens[r][column]:
                return False
        # if queens[:cur_row][column].count('Q'):
        #     return False
        # 右对角线，有Q返回False
        for r, c in zip(range(cur_row - 1, 0, -1), range(column)):
            if queens[r][c]:
                return False
        # 左对角线，有Q返回False
        for r, c in zip(range(cur_row), range(column)):
            if queens[r][c]:
                return False
        return True


class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                print(queens)
                return
            for q in range(n):
                # 关键部分
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    s = Solution2()
    n = 2
    # q = [['.'] * 4] * 4
    # q[0][2] = 'Q'
    # q[1][2] = 'Q'
    # print(s.is_valide(1, 2, q))

    print(s.solveNQueens(n))
