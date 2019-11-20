# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-19 19:56
# @Author   : Fabrice LI
# @File     : 20191119_459_closest_number_in_sorted_array.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a target number and an integer array A sorted in ascending order,
#               find the index i in A such that A[i] is closest to the given target.
#
#               Return -1 if there is no element in the array.
#Reference:**********************************************
"""
Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.

Given [1, 2, 3] and target = 2, return 1.

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.

Challenge
O(logn) time complexity.
"""
class Solution:
    def findClosetNumber(self, nums, target):
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] - target > nums[right] - target:
            return right
        else:
            return left


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 3, 4, 6]
    target = 5
    print(s.findClosetNumber(nums, target))
