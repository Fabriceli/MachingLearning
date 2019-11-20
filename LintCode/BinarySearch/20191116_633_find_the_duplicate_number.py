# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-11-16 10:26
# @Author   : Fabrice LI
# @File     : 20191116_633_find_the_duplicate_number.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
#               prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
#               find the duplicate one.
# Reference:**********************************************
'''
E.g
Input: [1,3,4,2,2]
Output: 2

Input: [3,1,3,4,2]
Output: 3

1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1
        # 不需要排序
        while left + 1 < right:
            mid = (left + right) >> 1
            # 寻找缩减条件
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # 左右缩减条件
            if count > mid:
                right = mid
            else:
                left = mid
        return left + 1

    def findDuplicate2(self, nums):
        first = 1
        last = len(nums) - 1
        while first < last:
            mid = first + (last - first) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                last = mid
            else:
                first = mid + 1
        return first


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1]
    print(s.findDuplicate(nums))
