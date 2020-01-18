# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-18 09:41
# @Author   : Fabrice LI
# @File     : 20200117_512_decode_ways.py
# @User     : liyihao
# @Software : PyCharm
# @Description: A message containing letters from A-Z is being encoded to numbers using the following mapping:
#               'A' -> 1
#               'B' -> 2
#               ...
#               'Z' -> 26
#Reference:**********************************************
"""
Given an encoded message containing digits, determine the total number of ways to decode it.

Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).

Input: "10"
Output: 1
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size <= 0:
            return 0
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1

        for i in range(1, size + 1):
            if '1' <= s[i - 1] <= '9':
                dp[i] += dp[i - 1]
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        return dp[size]


if __name__ == '__main__':
    s = Solution()
    st = "1230"
    print(s.numDecodings(st))
