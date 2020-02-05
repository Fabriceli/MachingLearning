# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2020-02-01 16:26
# @Author   : Fabrice LI
# @File     : 20200130_77_longest_common_subsequence.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two strings, find the longest common subsequence (LCS).
#
#               Your code should return the length of LCS.
# Reference:**********************************************
"""
Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1

	Explanation:
	LCS is 'A' or  'D' or 'C'


Example 2:
	Input: "ABCD" and "EACB"
	Output:  2

	Explanation:
	LCS is "AC"
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        columns = len(text2)

        dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                if text1[row - 1] == text2[column - 1]:
                    dp[row][column] = max(dp[row - 1][column], dp[row][column - 1], dp[row - 1][column - 1] + 1)
                else:
                    dp[row][column] = max(dp[row - 1][column], dp[row][column - 1])

        return dp[rows][columns]


if __name__ == '__main__':
    s = Solution()
    text1 = 'ABCD'
    text2 = 'EACB'
    print(s.longestCommonSubsequence(text1, text2))
