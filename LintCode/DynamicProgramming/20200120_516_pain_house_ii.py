# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-20 10:32
# @Author   : Fabrice LI
# @File     : 20200120_516_pain_house_ii.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are a row of n houses, each house can be painted with one of the k colors.
#               The cost of painting each house with a certain color is different.
#               You have to paint all the houses such that no two adjacent houses have the same color.
#
#               The cost of painting each house with a certain color is represented by a n x k cost matrix.
#               For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the
#               cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#Reference:**********************************************
"""
Input:
costs = [[14,2,11],[11,14,5],[14,3,10]]
Output: 10
Explanation:
The three house use color [1,2,1] for each house. The total cost is 10.

Input:
costs = [[5]]
Output: 5
Explanation:
There is only one color and one house.

Challenge
Could you solve it in O(nk)?
"""
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        nums_houses = len(costs)
        nums_colors = len(costs[0])
        index_first_min_cost = 0
        dp = [[0 for _ in range(nums_colors)] for _ in range(nums_houses + 1)]

        for index_house in range(1, nums_houses + 1):
            first_min_cost = float('inf')
            second_min_cost = float('inf')
            for index_color in range(nums_colors):
                if dp[index_house - 1][index_color] < first_min_cost:
                    second_min_cost = first_min_cost
                    first_min_cost = dp[index_house - 1][index_color]
                    index_first_min_cost = index_color
                elif dp[index_house - 1][index_color] < second_min_cost:
                    second_min_cost = dp[index_house - 1][index_color]

            for color in range(nums_colors):
                dp[index_house][color] = costs[index_house - 1][color]
                if color != index_first_min_cost:
                    dp[index_house][color] += first_min_cost
                else:
                    dp[index_house][color] += second_min_cost
        return min(dp[-1])


if __name__ == '__main__':
    s = Solution()
    # costs = [[7,19,11,3,7,15,17,5,6,18,1,15,18,11],[13,18,18,8,13,12,11,13,4,8,2,4,5,20],[14,5,18,4,7,6,1,6,11,6,16,6,13,17],[18,17,11,3,12,4,8,6,2,7,10,9,19,3],[4,3,2,14,11,15,18,1,17,1,6,14,14,9],[9,13,15,14,5,1,1,6,11,15,16,12,10,18],[19,2,11,3,13,4,13,7,16,16,20,18,20,8],[8,19,20,9,18,13,17,1,2,4,3,20,15,9],[9,10,11,6,14,20,4,1,5,15,13,10,13,5],[13,11,9,11,9,16,3,19,1,11,6,7,12,13],[14,1,15,14,11,12,7,14,12,11,6,9,5,5]]
    costs = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    print(s.minCostII(costs))
