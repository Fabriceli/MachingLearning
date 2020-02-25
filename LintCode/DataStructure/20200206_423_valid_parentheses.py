# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-07 10:17
# @Author   : Fabrice LI
# @File     : 20200206_423_valid_parentheses.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
#               string is valid.
#
#               The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are
#               not.
#Reference:**********************************************
"""
Input: "([)]"
Output: False

Input: "()[]{}"
Output: True

Challenge
Use O(n) time, n is the number of parentheses.
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            if c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
        if not stack:
            return True
        return False
        # if not s:
        #     return False
        # stack = 0
        # for p in s:
        #     if p == '(':
        #         stack += 1
        #     else:
        #         if not stack:
        #             return False
        #         stack -= 1
        #
        # if not stack:
        #     return True
        # else:
        #     return False

    def longest(self, s: str) -> int:
        if not s:
            return False
        res = 0
        stack = deque()

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    left = stack.pop()
                    res = max(res, i - left + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    st = '()((())'
    print(s.isValid(st))
    print(s.longest(st))
