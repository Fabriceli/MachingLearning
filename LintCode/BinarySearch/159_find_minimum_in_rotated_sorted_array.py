# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-17 17:13
# @Author   : Fabrice LI
# @File     : 159_find_minimum_in_rotated_sorted_array.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#               (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#               Find the minimum element.
# Reference:**********************************************
'''
E.g
Input：[4, 5, 6, 7, 0, 1, 2]
Output：0
Explanation：
The minimum value in an array is 0.

Input：[2,1]
Output：1
Explanation：
The minimum value in an array is 1.

'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            print("d", nums[mid], left, right)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]


if __name__ == '__main__':
    nums = [7, 7, 7, 8, 1, 1, 2, 2, 3, 4, 5, 6]
    s = Solution()
    print(s.findMin(nums))
