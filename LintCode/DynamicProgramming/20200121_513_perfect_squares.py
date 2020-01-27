# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-24 14:30
# @Author   : Fabrice LI
# @File     : 20200121_513_perfect_squares.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#Reference:**********************************************
"""
Input: 12
Output: 3
Explanation: 4 + 4 + 4

Input: 13
Output: 2
Explanation: 4 + 9
"""
class Solution:
    def numSquares(self, n: int) -> int:
        if not n or n <= 0:
            return 0

        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int( i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    n = 4564343
    print(s.numSquares(n))
