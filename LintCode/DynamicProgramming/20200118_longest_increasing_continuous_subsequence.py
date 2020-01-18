# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-18 12:00
# @Author   : Fabrice LI
# @File     : 20200118_longest_increasing_continuous_subsequence.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Give an integer array，find the longest increasing continuous subsequence in this array.
#
#               An increasing continuous subsequence:
#
#               Can be from right to left or from left to right.
#               Indices of the integers in the subsequence should be continuous.
#Reference:**********************************************
"""
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.

"""
from typing import List


class Solution:
    def get_lcis(self, nums):
        size = len(nums)
        dp = [1 for _ in range(size)]

        res = 0
        for i in range(size):
            if i > 0 and nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1]
            res = max(res, dp[i])
        return res

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        res1 = self.get_lcis(nums)
        res2 = self.get_lcis(nums[::-1])
        return max(res1, res2)


if __name__ == '__main__':
    s = Solution()
    nums = [2,2,2,2,2]
    print(s.findLengthOfLCIS(nums))
