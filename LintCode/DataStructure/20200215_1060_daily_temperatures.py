# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-18 10:29
# @Author   : Fabrice LI
# @File     : 20200215_1060_daily_temperatures.py
# @User     : liyihao
# @Software : PyCharm
# @Description: todo
#Reference:**********************************************
"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you
would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be
[1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range
[30, 100].

"""
from typing import List

"""
思路：
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        size = len(T)
        if size <= 1:
            return T
        res = [0] * size
        stack = [0]
        left = 1
        while stack:
            if left >= size:
                stack.pop()
                continue
            if T[stack[-1]] < T[left]:
                while stack and T[stack[-1]] < T[left]:
                    index = stack.pop()
                    res[index] = left - index
                stack.append(left)
                left += 1
            else:
                stack.append(left)
                left += 1
        return res

    def dailyTemperatures2(self, T: List[int]) -> List[int]:
        size = len(T)
        if size <= 1:
            return T
        stack = [0]
        res = [0] * size

        for i in range(1, size):
            while stack and T[stack[-1]] < T[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures2(T))
