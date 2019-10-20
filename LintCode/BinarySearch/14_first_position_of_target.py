# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-18 12:29
# @Author   : Fabrice LI
# @File     : 14_first_position_of_target.py
# @User     : liyihao
# @Software: PyCharm
# @Description: For a given sorted array (ascending order) and a target number,
#               find the first index of this number in O(log n) time complexity.
#
#               If the target number does not exist in the array, return -1.
# Reference:**********************************************
'''
E.g
Input:  [1,4,4,5,7,7,8,9,9,10]，1
Output: 0
Explanation:
the first index of  1 is 0.

Input: [1, 2, 3, 3, 4, 5, 10]，3
Output: 2
Explanation:
the first index of 3 is 2.

Input: [1, 2, 3, 3, 4, 5, 10]，6
Output: -1
Explanation:
Not exist 6 in array.

Challenge
If the count of numbers is bigger than 2^32, can your code work properly?
'''


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid
        return left if nums[left] == target else -1

    # 二分固定模版，牢记
    def binarySearchCommu(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [2]
    target = 2
    print(s.binarySearchCommu(nums, target))
