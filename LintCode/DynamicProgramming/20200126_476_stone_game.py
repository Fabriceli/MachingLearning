# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-29 16:31
# @Author   : Fabrice LI
# @File     : 20200126_476_stone_game.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
#
#               The goal is to merge the stones in one pile observing the following rules:
#
#               At each step of the game,the player can merge two adjacent piles to a new pile.
#               The score is the number of stones in the new pile.
#               You are to determine the minimum of the total score.
#Reference:**********************************************
"""
Input: [3, 4, 3]
Output: 17

Input: [4, 1, 1, 4]
Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
"""

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        if not A:
            return 0
        size = len(A)
        # 定义状态函数，dp[i][j]表示从第i个石子到第j个石子合并在一起的最小花费
        dp = [[0 for _ in range(size)] for _ in range(size)]
        visited = [[False for _ in range(size)] for _ in range(size)]
        sum_a = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            sum_a[i][i] = A[i]
            for j in range(i + 1, size):
                sum_a[i][j] = sum_a[i][j - 1] + A[j]
        return self.search(0, size - 1, dp, visited, sum_a)

    def search(self, left, right, dp, visited, sum_a):
        if visited[left][right] or left == right:
            visited[left][right] = True
            return dp[left][right]
        visited[left][right] = True
        dp[left][right] = float('inf')
        for i in range(left, right):
            dp[left][right] = min(dp[left][right],
                                  self.search(left, i, dp, visited, sum_a)
                                  + self.search(i + 1, right, dp, visited, sum_a)
                                  + sum_a[left][right])
        return dp[left][right]


if __name__ == '__main__':
    s = Solution()
    A = [4, 1, 1, 4]
    print(s.stoneGame(A))
