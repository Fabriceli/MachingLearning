# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-31 12:37
# @Author   : Fabrice LI
# @File     : 20191228_547_intersection_of_two_arrays.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two arrays, write a function to compute their intersection.
#Reference:**********************************************
"""
Each element in the result must be unique.
The order of the results needs to be ascending

Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2],
Output: [2].

Input: nums1 = [1, 2], nums2 = [2],
Output: [2].

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Challenge
Can you implement it in three different algorithms?
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1. hash map
        2. sort & merge
        3. sort & binary search
        :param nums1:
        :param nums2:
        :return:
        """
        # 2. sort and merge
        nums1.sort()
        nums2.sort()
        l1 = len(nums1) - 1
        l2 = len(nums2) - 1
        l3 = 0

        result = []

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] == nums2[l2]:
                if l3 == 0 or result[l3 - 1] != nums1[l1]:
                    result.append(nums1[l1])
                    l3 += 1
                l1 -= 1
                    # l2 -= 1
            elif nums1[l1] > nums2[l2]:
                l1 -= 1
            else:
                l2 -= 1

        return result

    def intersection_sort_binary(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        sort & binary search
        :param nums1:
        :param nums2:
        :return:
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 > l2:
            nums2.sort()


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersection(nums1, nums2))
