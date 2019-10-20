# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-22 15:54
# @Author   : Fabrice LI
# @File     : 160_find_minimum_in_rotated_sorted_array_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#               (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#               Find the minimum element.
#               The array may contain duplicates.
#Reference:**********************************************
'''
E.g
Input :[2,1]
Output : 1.

Input :[4,4,5,6,7,0,1,2]
Output : 0.

'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right + left) >> 1
            if nums[mid] == nums[right]: # 关键点，不会丢失最小值，同时缩减右边界
                right = right - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1]
    print(s.findMin(nums))
