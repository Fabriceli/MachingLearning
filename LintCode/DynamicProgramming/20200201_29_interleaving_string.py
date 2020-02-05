# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-04 13:10
# @Author   : Fabrice LI
# @File     : 20200201_29_interleaving_string.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
#Reference:**********************************************
"""
Input:
"aabcc"
"dbbca"
"aadbbcbcac"
Output:
true

Input:
""
""
"1"
Output:
false

Input:
"aabcc"
"dbbca"
"aadbbbaccc"
Output:
false

Challenge
O(n2) time or better
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        rows = len(s2)
        columns = len(s1)
        size3 = len(s3)
        if rows + columns != size3:
            return False

        dp = [[False for _ in range(columns + 1)] for _ in range(rows + 1)]

        # 初始化状态方程
        dp[0][0] = True
        for r in range(1, rows + 1):
            if dp[r - 1][0] and s3[r - 1] == s2[r - 1]:
                dp[r][0] = True

        for c in range(1, columns + 1):
            if dp[0][c - 1] and s3[c - 1] == s1[c - 1]:
                dp[0][c] = True

        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                dp[r][c] = (dp[r - 1][c] and s2[r - 1] == s3[r + c - 1]) \
                           or (dp[r][c - 1] and s1[c - 1] == s3[r + c - 1]) \
                           or (dp[r - 1][c - 1] and (s2[r - 1] + s1[c - 1] == s3[r + c - 2:r + c]
                                                     or s1[c - 1] + s2[r - 1] == s3[r + c - 2:r + c]))
        for i in dp:
            print(i)
        return dp[rows][columns]


if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(s.isInterleave(s1, s2, s3))
