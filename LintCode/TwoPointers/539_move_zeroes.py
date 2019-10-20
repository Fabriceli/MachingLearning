# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-23 19:40
# @Author   : Fabrice LI
# @File     : 539_move_zeroes.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array nums, write a function to move all 0's to
#               the end of it while maintaining the relative order of the non-zero elements.
#               1. You must do this in-place without making a copy of the array.
#               2. Minimize the total number of operations.
#Reference:**********************************************
'''
E.g
Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
'''


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums:
            return 0
        end = len(nums)
        j = 0
        for i in range(end):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 3, 1]
    print(s.moveZeroes(nums))
