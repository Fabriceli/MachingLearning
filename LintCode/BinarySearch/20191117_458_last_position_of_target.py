# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-17 21:35
# @Author   : Fabrice LI
# @File     : 20191117_458_last_position_of_target.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Find the last position of a target number in a sorted array. Return -1 if target does not exist.
#Reference:**********************************************
'''
E.g
Given [1, 2, 2, 4, 5, 5].
For target = 2, return 2.
For target = 5, return 5.
For target = 6, return -1
'''
from typing import List


class Solution:
    def findLastPosition(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 4, 5, 5]
    target = 6
    print(s.findLastPosition(nums, target))
