# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-21 17:34
# @Author   : Fabrice LI
# @File     : 457_classical_binary_search.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Find any position of a target number in a sorted array. Return -1 if target does not exist.
# Reference:**********************************************
'''
E.g
Input: nums = [1,2,2,4,5,5], target = 2
Output: 1 or 2

Input: nums = [1,2,2,4,5,5], target = 6
Output: -1

Challenge
O(logn) time
'''


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = []
    target = 3
    print(s.findPosition(nums, target))
