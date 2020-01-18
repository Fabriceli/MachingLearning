# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-18 00:13
# @Author   : Fabrice LI
# @File     : 20200116_515_paint_house.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
#               The cost of painting each house with a certain color is different. You have to paint all the houses such
#               that no two adjacent houses have the same color, and you need to cost the least.
#               Return the minimum cost.
#
#               The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
#               For example, costs[0][0] is the cost of painting house 0 with color red;
#               costs[1][2] is the cost of painting house 1 with color green, and so on...
#               Find the minimum cost to paint all houses.
#Reference:**********************************************
"""
Input: [[14,2,11],[11,14,5],[14,3,10]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.

Input: [[1,2,3],[1,4,6]]
Output: 3
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        nums_houses = len(costs)
        if nums_houses <= 0:
            return 0
        # define dp, 每栋房子的涂上三种颜色的最小花费
        dp = [[0, 0, 0] for _ in range(nums_houses + 1)]

        for i in range(1, nums_houses + 1):
            dp[i][0] = min(dp[i - 1][1] + costs[i - 1][1], dp[i - 1][2] + costs[i - 1][2])
            dp[i][1] = min(dp[i - 1][2] + costs[i - 1][2], dp[i - 1][0] + costs[i - 1][0])
            dp[i][2] = min(dp[i - 1][1] + costs[i - 1][1], dp[i - 1][0] + costs[i - 1][0])

        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    costs = [[1,2,3],[1,4,6]]
    print(s.minCost(costs))


