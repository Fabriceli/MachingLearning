# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-30 15:23
# @Author   : Fabrice LI
# @File     : 20200127_burst_ballon.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented
#               by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get
#               nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After
#               the burst, the left and right then becomes adjacent.
#
#               Find the maximum coins you can collect by bursting the balloons wisely.
#Reference:**********************************************
"""
- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Input：[4, 1, 5, 10]
Output：270
Explanation：
nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]   burst 5, get coins 4 * 5 * 10 = 200
nums = [4, 10]    burst 4, get coins 1 * 4 * 10 = 40
nums = [10]    burst 10, get coins 1 * 10 * 1 = 10
Total coins 20 + 200 + 40 + 10 = 270

Input：[3,1,5]
Output：35
Explanation：
nums = [3, 1, 5] burst 1, get coins 3 * 1 * 5 = 15
nums = [3, 5] burst 3, get coins 1 * 3 * 5 = 15
nums = [5] burst 5, get coins 1 * 5 * 1 = 5
Total coins 15 + 15 + 5  = 35
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        nums = [1, *nums, 1]

        dp = [[0 for _ in range(size + 2)] for _ in range(size + 2)]
        visited = [[False for _ in range(size + 2)] for _ in range(size + 2)]
        return self.search(1, size, dp, visited, nums)

    def search(self, left, right, dp, visited, nums):
        if visited[left][right]:
            return dp[left][right]
        visited[left][right] = True
        for k in range(left, right + 1):
            mi_value = nums[left - 1] * nums[k] * nums[right + 1]
            left_value = self.search(left, k - 1, dp, visited, nums)
            right_value = self.search(k + 1, right, dp, visited, nums)
            dp[left][right] = max(dp[left][right],  left_value + mi_value + right_value)
        return dp[left][right]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2]
    print(s.maxCoins(nums))
