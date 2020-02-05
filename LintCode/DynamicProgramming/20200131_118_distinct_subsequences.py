# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-01 19:35
# @Author   : Fabrice LI
# @File     : 20200131_118_distinct_subsequences.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two strings S and T. Count the number of distinct subsequences of S which equals T.
#
#               A subsequence of a string is a new string which is formed from the original string by deleting
#               some (can be none) of the characters without disturbing the relative positions of the remaining
#               characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not)
#Reference:**********************************************
"""
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation: You could remove any 'b' in S, so there are 3 ways to get T.

Input: S = "abcd", T = ""
Output: 1
Explanation: There is only 1 way to get T - remove all chars in S.

Challenge
Do it in O(n^2n
​2
​​ ) time and O(n) memory.

O(n^2n
​2
​​ ) memory is also acceptable if you do not know how to optimize memory.
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(t)
        columns = len(s)
        dp = [[0 for _ in range(columns + 1)] for _ in range(2)]
        for c in range(columns + 1):
            dp[0][c] = 1

        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                dp[r % 2][0] = 0
                if s[c - 1] == t[r - 1]:
                    dp[r % 2][c] = dp[(r - 1) % 2][c - 1] + dp[r % 2][c - 1]
                else:
                    dp[r % 2][c] = dp[r % 2][c - 1]

        return dp[rows % 2][columns]


if __name__ == '__main__':
    s = Solution()
    st = 'babgbag'
    t = 'bag'
    a = 'rabbbit'
    b = 'rabbit'

    print(s.numDistinct(st, t))
    print(s.numDistinct(a, b))
