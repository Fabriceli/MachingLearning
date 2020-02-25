# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-18 11:34
# @Author   : Fabrice LI
# @File     : 20200216_remove_duplicates_from_sorted_array.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a sorted array, 'remove' the duplicates in place such that each element appear only once and
#               return the 'new' length.
#
#               Do not allocate extra space for another array, you must do this in place with constant memory.
#Reference:**********************************************
"""
Input:  []
Output: 0

Input:  [1,1,2]
Output: 2
Explanation:  uniqued array: [1,2]

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        slow = 0
        fast = slow + 1
        du = 0

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                du += 1
                # fast += 1
                nums.remove(nums[fast])
            else:
                slow = fast
                fast = slow + 1
        print(nums)
        return size - du

    def removeDuplicates2(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        print(nums)
        return slow + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print(s.removeDuplicates2(nums))
