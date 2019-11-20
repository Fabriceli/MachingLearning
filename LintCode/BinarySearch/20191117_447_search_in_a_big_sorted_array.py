# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-17 21:42
# @Author   : Fabrice LI
# @File     : 20191117_447_search_in_a_big_sorted_array.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a big sorted array with positive integers sorted by ascending order.
#               The array is so big so that you can not get the length of the whole array directly,
#               and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
#               Find the first index of a target number. Your algorithm should be in O(log k),
#               where k is the first index of the target number.
#               Return -1, if the number doesn't exist in the array.
#Reference:**********************************************
'''
Notice
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2,147,483,647.

Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.
'''

from typing import List


class Solution:
    def searchBigArray(self, nums, target: int) -> int:
        if len(nums) <= 0:
            return -1
        left = 0
        # 先找右边界
        right = 1
        while nums[right] <= target:
            right >>= 1

        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
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
    nums = [1, 3, 6, 9, 21, 24, 28, 29, 30, 36, 39, 40]
    target = 21
    print(s.searchBigArray(nums, target))
