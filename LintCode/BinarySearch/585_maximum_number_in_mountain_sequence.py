# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-18 10:45
# @Author   : Fabrice LI
# @File     : 585_maximum_number_in_mountain_sequence.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.
# Reference:**********************************************
'''
E.g
Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8

Input: nums = [10, 9, 8, 7],
Output: 10
'''


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) >> 1
            # 因为先升序后降序，只要找到升序的在左边还是在右边就可以不断夹逼，左右边界
            # 注意：理解题意，题目提供了条件
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 5, 3]
    print(s.mountainSequence(nums))
