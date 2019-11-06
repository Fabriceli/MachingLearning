# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-06 22:09
# @Author   : Fabrice LI
# @File     : 20191106_34_n-queens_ii.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Follow up for N-Queens problem.
#
#               Now, instead outputting board configurations,
#               return the total number of distinct solutions.
#Reference:**********************************************
'''
E.g
Input: n=1
Output: 1
Explanation:
1:
1

Input: n=4
Output: 2
Explanation:
1:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
2:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
'''

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n):
        def dfs(queens, xy_diff, xy_sum):
            y = len(queens)
            if y == n:
                self.res += 1
                return
            for x in range(n):
                if x not in queens and x - y not in xy_diff and x + y not in xy_sum:
                    dfs(queens + [x], xy_diff + [x - y], xy_sum + [x + y])

        dfs([], [], [])
        return self.res


if __name__ == '__main__':
    s = Solution()
    n = 4
    print(s.totalNQueens(n))
