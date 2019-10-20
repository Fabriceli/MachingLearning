# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-22 16:13
# @Author   : Fabrice LI
# @File     : 63_search_in_rotated_sorted_array_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#               (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#               You are given a target value to search. If found in the array return true, otherwise return false.
#Reference:**********************************************
'''
E.g
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        if nums[left] == target or nums[right] == target:
            return True
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                # 左边升序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 1]
    target = 0
    print(s.search(nums, target))
