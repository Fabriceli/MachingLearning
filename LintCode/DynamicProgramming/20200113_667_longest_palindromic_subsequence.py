# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-14 00:47
# @Author   : Fabrice LI
# @File     : 20200113_667_longest_palindromic_subsequence.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string s, find the longest palindromic subsequence's length in s.
#               You may assume that the maximum length of s is 1000.
#Reference:**********************************************
"""
Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".

Input: "bbbbb"
Output: 5
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return max(dp[0])


if __name__ == '__main__':
    s = Solution()
    st = 'b'
    print(s.longestPalindromeSubseq(st))
