# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-31 10:55
# @Author   : Fabrice LI
# @File     : 20200129_119_edit_distance.py
# @User     : liyihao
# @Software : PyCharm
# @Description: todo
#Reference:**********************************************
"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

Input:
"horse"
"ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input:
"intention"
"execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        columns = len(word1) # source
        rows = len(word2) # target

        dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
        for c in range(columns + 1):
            dp[0][c] = c
        for r in range(rows + 1):
            dp[r][0] = r

        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if word1[c - 1] == word2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1

        return dp[rows][columns]


if __name__ == '__main__':
    s = Solution()
    word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
    word2 = "ultramicroscopically"
    print(s.minDistance(word1, word2))
