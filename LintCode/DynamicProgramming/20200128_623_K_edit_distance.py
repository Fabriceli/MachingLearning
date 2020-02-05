# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-31 10:42
# @Author   : Fabrice LI
# @File     : 20200128_623_K_edit_distance.py
# @User     : liyihao
# @Software : PyCharm
# @Description: todo
#Reference:**********************************************
"""
Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit
distance with the target no greater than k.

You have the following 3 operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

Given words = `["abc", "abd", "abcd", "adc"]` and target = `"ac"`, k = `1`
Return `["abc", "adc"]`
Input:
["abc", "abd", "abcd", "adc"]
"ac"
1
Output:
["abc","adc"]

Explanation:
"abc" remove "b"
"adc" remove "d"


Input:
["acc","abcd","ade","abbcd"]
"abc"
2
Output:
["acc","abcd","ade","abbcd"]

Explanation:
"acc" turns "c" into "b"
"abcd" remove "d"
"ade" turns "d" into "b" turns "e" into "c"
"abbcd" gets rid of "b" and "d"
"""
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        res = []
        for word in words:
            distance = self.minDistance(word, target)
            if distance <= k:
                res.append(word)
        return res

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
    words = ["abc", "abd", "abcd", "adc"]
    target = "ac"
    k = 1
    print(s.kDistance(words, target, k))
