# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-02 20:17
# @Author   : Fabrice LI
# @File     : 20200102_76_longest_increasing_subsequence.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a sequence of integers, find the longest increasing subsequence (LIS).
#
#               You code should return the length of the LIS.
#Reference:**********************************************
"""
What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's
elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example 1:
	Input:  [5,4,1,2,3]
	Output:  3

	Explanation:
	LIS is [1,2,3]


Example 2:
	Input: [4,2,4,5,3,7]
	Output:  4

	Explanation:
	LIS is [2,4,5,7]


Challenge
Time complexity O(n^2) or O(nlogn)
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1 for _ in range(length)]

        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(nums))
