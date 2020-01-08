# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2020-01-03 21:58
# @Author   : Fabrice LI
# @File     : 20200103_109_triangle.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a triangle, find the minimum path sum from top to bottom.
#               Each step you may move to adjacent numbers on the row below.
# Reference:**********************************************
"""
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Input the following triangle:
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
Explanation: The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Input the following triangle:
[
     [2],
    [3,2],
   [6,5,7],
  [4,4,8,1]
]
Output: 12
Explanation: The minimum path sum from top to bottom is 12 (i.e., 2 + 2 + 7 + 1 = 12).


"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        # 1. 定义状态：
        dp = [num for num in triangle]


        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if 1 <= j < len(triangle[i - 1]):
                    dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == len(triangle[i - 1]):
                    dp[i][j] += dp[i - 1][j - 1]

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(s.minimumTotal(triangle))
