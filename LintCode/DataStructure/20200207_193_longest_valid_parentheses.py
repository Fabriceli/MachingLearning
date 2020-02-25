# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-07 17:05
# @Author   : Fabrice LI
# @File     : 20200207_193_longest_valid_parentheses.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string containing just the characters '(' and ')', find the length of the longest valid
#               (well-formed) parentheses substring.
#Reference:**********************************************
"""
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        # stack = deque()
        #
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         if stack:
        #             left = stack.pop()
        #             res = max(res, i - left + 1)
        # return res
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1

            if left == right:
                res = max(res, left * 2)
            pass




if __name__ == '__main__':
    s = Solution()
    st = ')()())'
    print(s.longestValidParentheses(st))
