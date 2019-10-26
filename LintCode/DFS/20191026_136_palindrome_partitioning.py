# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-10-26 14:46
# @Author   : Fabrice LI
# @File     : 20191026_136_palindrome_partitioning.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string s. Partition s such that every substring in the partition is a palindrome.
#               Return all possible palindrome partitioning of s.
#
#               1. Different partitionings can be in any order.
#               2. Each substring must be a continuous segment of s.
# Reference:**********************************************
'''
E.g
Input: "a"
Output: [["a"]]
Explanation: Only 1 char in the string, only 1 way to split it (itself).

Input: "aab"
Output: [["aa", "b"], ["a", "a", "b"]]
Explanation: There are 2 ways to split "aab".
    1. Split "aab" into "aa" and "b", both palindrome.
    2. Split "aab" into "a", "a", and "b", all palindrome.
'''
from typing import List


class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if not s:
            return [[]]
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]

        for r in range(length):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
        res = []
        def dfs(left, tempres):
            if left == length:
                res.append(tempres)
            for right in range(left, length):
                if dp[left][right]:
                    dfs(right + 1, tempres + [s[left:right + 1]])
        dfs(0, [])
        return res


if __name__ == '__main__':
    s = 'aab'
    res = Solution()
    print(res.partition(s))
