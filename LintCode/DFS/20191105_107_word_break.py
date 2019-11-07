# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-11-06 22:37
# @Author   : Fabrice LI
# @File     : 20191105_107_word_break.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string s and a dictionary of words dict,
#               determine if s can be broken into a space-separated sequence of one or more dictionary words.
# Reference:**********************************************
'''
E.g
Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true
'''


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        if not len(s):
            return False
        words = {word for word in dict}
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for right in range(1, len(s) + 1):
            for left in range(right):
                if dp[left] and s[left:right] in words:
                    dp[right] = True
                    break
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    string = "lintcode"
    dict = ["lint", "code"]
    print(s.wordBreak(string, dict))
