# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-01 15:49
# @Author   : Fabrice LI
# @File     : 20191101_582_word_break_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string s and a dictionary of words dict,
#               add spaces in s to construct a sentence where each word is a valid dictionary word.
#               Return all such possible sentences.
#Reference:**********************************************
'''
E.g
Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".

Input："a"，[]
Output：[]
Explanation：dict is null.
'''
from collections import deque


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        if not s:
            return []
        words = {word for word in wordDict}

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1

        for r in range(1, len(s) + 1):
            for l in range(r):
                if dp[l] and s[l:r] in words:
                    dp[r] = 1
                    break
        print(dp)
        res = []
        # 最后一位dp状态是1才会有解，否则无法分割
        if dp[-1]:
            queue = deque()
            self.dfs(s, len(s), words, res, queue, dp)
        return res

    def dfs(self, s, length, words, res, path, dp):
        if length == 0:
            res.append(' '.join(path))
            return
        for i in range(length):
            if dp[i]:
                suffix = s[i:length]
                if suffix in words:
                    path.appendleft(suffix)
                    self.dfs(s, i, words, res, path, dp)
                    path.popleft()


if __name__ == '__main__':
    s = Solution()
    string = "lintcode"
    wordDict = ["de", "ding", "co", "code", "lint", "in"]
    print(s.wordBreak(string, wordDict))
