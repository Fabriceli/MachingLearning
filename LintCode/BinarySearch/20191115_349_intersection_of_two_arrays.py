# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-15 12:33
# @Author   : Fabrice LI
# @File     : 20191115_349_intersection_of_two_arrays.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two arrays, write a function to compute their intersection.
#Reference:**********************************************
'''
E.g
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Each element in the result must be unique.
The result can be in any order.
'''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= 0 or len(nums2) <=0:
            return []
        res = set()
        nums1.sort()
        nums2.sort()
        nums1_left = 0
        nums2_left = 0
        while nums1_left < len(nums1) and nums2_left < len(nums2):
            if nums1[nums1_left] == nums2[nums2_left]:
                res.add(nums1[nums1_left])
                nums1_left += 1
                nums2_left += 1
            elif nums1[nums1_left] > nums2[nums2_left]:
                nums2_left += 1
            else:
                nums1_left += 1
        return list(res)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersection(nums1, nums2))
