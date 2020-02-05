# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-04 17:33
# @Author   : Fabrice LI
# @File     : 20200203_588_partition_equal_subset_sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a non-empty array containing only positive integers, find if the array can be partitioned into
#               two subsets such that the sum of elements in both subsets is equal.
#Reference:**********************************************
"""
Each of the array element will not exceed 100.
The array size will not exceed 200.

Input: nums = [1, 5, 11, 5],
Output: true
Explanation:
two subsets: [1, 5, 5], [11]

Input: nums = [1, 2, 3, 9],
Output: false
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sum_nums = sum(nums)
        # 奇数
        if sum_nums & 1:
            return False
        half_sum = sum_nums >> 1

        can = self.get_half_sum(half_sum, nums)
        return can != 0

    def get_half_sum(self, half_sum, nums):
        rows = len(nums)
        columns = half_sum

        dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
        dp[0][0] = 1

        for r in range(rows +1):
            dp[r][0] = 1
            for c in range(1, columns + 1):
                dp[r][c] = dp[r - 1][c]
                if c >= nums[r - 1]:
                    dp[r][c] = dp[r - 1][c - nums[r - 1]] or dp[r - 1][c]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3,3,3,4,5]
    nums2 = [2, 2, 3, 5]
    print(s.canPartition(nums2))
