# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-26 00:37
# @Author   : Fabrice LI
# @File     : 20200122_837_palindromic_substrings.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string, your task is to count how many palindromic substrings in this string.
#               The substrings with different start indexes or end indexes are counted as different
#               substrings even they consist of same characters.
#Reference:**********************************************
"""
The input string length won't exceed 1000

Input: "abc"
Output: 3
Explanation:
3 palindromic strings: "a", "b", "c".

Input: "aba"
Output: 4
Explanation:
4 palindromic strings: "a", "b", "a", "aba".
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        res = 0
        for i in range(size-1, -1, -1):
            dp[i][i] = 1
            for j in range(i, size):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    st = "asjdhfa"
    print(s.countSubstrings(st))
