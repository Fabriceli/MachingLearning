# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-08 19:34
# @Author   : Fabrice LI
# @File     : 20200108_minimum_insertion_steps_to_make_a_string_palindrome.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string s. In one step you can insert any character at any index of the string.
#
#               Return the minimum number of steps to make s palindrome.
#
#               A Palindrome String is one that reads the same backward as well as forward.
#Reference:**********************************************
"""
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Input: s = "g"
Output: 0

Input: s = "no"
Output: 1


Constraints:
- 1 <= s.length <= 500
- All characters of s are lower case English letters.
"""
# DP, dp[i][j]表示i到j之间的最大回文串
# 状态转移方程：需要分类讨论，当s[i] == s[j]的时候dp[i][j] = dp[i+1][j-1] + 2:表示上一级的最大回文串加2
# 当s[i] != s[j]的时候dp[i][j] = max(dp[i+1][j], dp[i][j-1]),如果他们两不等，那就是说明，
# 上一级的最大回文串加上j字符或者加上i字符后的最大回文串。
# 初始条件dp[i][i]=1。求出最大回文串后，用字符串长度减去最大回文串就是最小插入字符次数
class Solution:
    def minInsertions(self, s: str) -> int:
        if not s or s == s[::-1]:
            return 0
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        for i in dp:
            print(i)
        return size - dp[0][size - 1]


if __name__ == '__main__':
    s = Solution()
    string = "zjveiiwvc"
    print(s.minInsertions(string))
