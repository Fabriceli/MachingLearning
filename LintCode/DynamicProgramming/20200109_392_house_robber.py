# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-10 00:46
# @Author   : Fabrice LI
# @File     : 20200109_392_house_robber.py
# @User     : liyihao
# @Software : PyCharm
# @Description: You are a professional robber planning to rob houses along a street.
#               Each house has a certain amount of money stashed, the only constraint
#               stopping you from robbing each of them is that adjacent houses have security
#               system connected and it will automatically contact the police if two adjacent
#               houses were broken into on the same night.
#
#               Given a list of non-negative integers representing the amount of money of each house,
#               determine the maximum amount of money you can rob tonight without alerting the police.
#Reference:**********************************************
"""
Input: [3, 8, 4]
Output: 8
Explanation: Just rob the second house.

Input: [5, 2, 1, 3]
Output: 8
Explanation: Rob the first and the last house.

Challenge
O(n) time and O(1) memory.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        dp = [0, 0, 0]
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, size + 1):
            dp[i%3] = max(dp[(i - 1)%3], dp[(i - 2)%3] + nums[i - 1])
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 1, 3]
    print(s.rob(nums))
