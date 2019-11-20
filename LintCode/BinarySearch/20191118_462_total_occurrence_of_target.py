# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-19 01:00
# @Author   : Fabrice LI
# @File     : 20191118_462_total_occurrence_of_target.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a target number and an integer array sorted in ascending order.
#               Find the total number of occurrences of target in the array.
#Reference:**********************************************
"""
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.

Challenge
Time complexity in O(logn)
"""

class Solution:
    def findAllOccu(self, nums, target):
        if len(nums) <= 0:
            return -1
        # find the left point
        left = 0
        right = len(nums) - 1
        index_left = -1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            index_left = left
        elif nums[right] == target:
            index_left = right
        if index_left == -1:
            return 0

        # find the right point
        left = 0
        right = len(nums) - 1
        index_right = -1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[right] == target:
            index_right = right
        elif nums[left] == target:
            index_right = left
        return index_right - index_left + 1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 4, 6]
    target = 5
    print(s.findAllOccu(nums, target))
