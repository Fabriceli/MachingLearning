# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2020-01-10 10:03
# @Author   : Fabrice LI
# @File     : 20200110_534_house_robber.py
# @User     : liyihao
# @Software : PyCharm
# @Description: After robbing those houses on that street, the thief has found himself
#               a new place for his thievery so that he will not get too much attention.
#               This time, all houses at this place are arranged in a circle. That means
#               the first house is the neighbor of the last one. Meanwhile, the security
#               system for these houses remain the same as for those in the previous street.
#
#               Given a list of non-negative integers representing the amount of money of
#               each house, determine the maximum amount of money you can rob tonight without alerting the police.
# Reference:**********************************************
"""
Input:  nums = [3,6,4]
Output: 6

Input:  nums = [2,3,2,3]
Output: 6
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # return max(self._rob(nums, 0, len(nums) - 2), self._rob(nums, 1, len(nums) - 1))
        return max(self._rob2(nums[1:]), self._rob2(nums[:len(nums) - 1]))

    def _rob(self, nums, start, end):
        if start == end:
            return nums[end]
        if start + 1 == end:
            return max(nums[start], nums[end])
        dp = [nums[start], max(nums[start], nums[start + 1])]

        for i in range(start + 2, end + 1):
            dp[i % 2] = max(dp[(i - 1) % 2], dp[(i - 2) % 2] + nums[i])
        return dp[end % 2]

    def _rob2(self, nums):
        dp = [0, nums[0]]

        for i in range(2, len(nums) + 1):
            dp[i%2] = max(dp[(i - 2)%2] + nums[i - 1], dp[(i - 1)%2])
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [1,7,9,2]
    print(s.rob(nums))
    print(s._rob(nums, 1, 3))
