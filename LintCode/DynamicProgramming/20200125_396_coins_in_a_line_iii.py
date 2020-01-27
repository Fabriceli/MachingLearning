# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-27 21:00
# @Author   : Fabrice LI
# @File     : 20200125_396_coins_in_a_line_iii.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are n coins in a line, and value of i-th coin is values[i].
#
#               Two players take turns to take a coin from one of the ends of the line until there are no more coins
#               left. The player with the larger amount of money wins.
#
#               Could you please decide the first player will win or lose?
#Reference:**********************************************
"""
Example

Given array A = [3,2,2], return true.
Given array A = [1,2,4], return true.
Given array A = [1,20,4], return false.
Challenge
Follow Up Question:
If n is even.
Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?
"""
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if not values:
            return False
        size = len(values)
        # dp[i][j]表示从i到j，先手能取到的最大价值总和
        dp = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
        visited = [[False for _ in range(size + 1)] for _ in range(size + 1)]
        values_sum = sum(values)

        return values_sum < 2 * self.search(0, size - 1, dp, visited, values)

    def search(self, left, right, dp, visited, values):
        if visited[left][right]:
            return dp[left][right]
        visited[left][right] = True
        if left > right:
            print(left)
            dp[left][right] = 0
        elif left == right:
            dp[left][right] = values[left]
        elif left + 1 == right:
            dp[left][right] = max(values[left], values[right])
        else:
            left_nums = min(self.search(left + 2, right, dp, visited, values),
                       self.search(left + 1, right - 1, dp, visited, values)) + values[left]
            right_nums = min(self.search(left, right - 2, dp, visited, values),
                        self.search(left + 1, right - 1, dp, visited, values)) + values[right]
            dp[left][right] = max(left_nums, right_nums)
        return dp[left][right]


if __name__ == '__main__':
    s = Solution()
    values = [3, 2, 2]
    print(s.firstWillWin(values))
