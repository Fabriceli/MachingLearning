# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-25 00:32
# @Author   : Fabrice LI
# @File     : 608_two_sum_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array of integers that is already sorted in ascending order,
#               find two numbers such that they add up to a specific target number.
#
#               The function twoSum should return indices of the two numbers such that
#               they add up to the target, where index1 must be less than index2.
#               Please note that your returned answers (both index1 and index2) are not zero-based.
#Reference:**********************************************
'''
E.g
Input: nums = [2, 7, 11, 15], target = 9
Output: [1, 2]

Input: nums = [2,3], target = 5
Output: [1, 2]
'''

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3]
    target = 5
    print(s.twoSum(nums, target))
