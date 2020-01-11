# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-09 19:06
# @Author   : Fabrice LI
# @File     : 20200109_41_maximum_subarray.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an integer array nums, find the contiguous subarray (containing at least one number)
#               which has the largest sum and return its sum.
#Reference:**********************************************
"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.

"""
from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        dp = [0 for _ in range(size)]
        result = float('-inf')
        dp[0] = nums[0]

        for i in range(size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
