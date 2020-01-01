# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-31 01:01
# @Author   : Fabrice LI
# @File     : 20191229_64_merge_sorted_array.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two sorted integer arrays A and B, merge B into A as one sorted array.
#Reference:**********************************************
"""
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.

Input：[1, 2, 3] 3  [4,5]  2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]

Input：[1,2,5] 3 [3,4] 2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length1 = m - 1
        length2 = n - 1
        length = m + n - 1

        while length1 >= 0 and length2 >= 0:
            if nums1[length1] > nums2[length2]:
                nums1[length] = nums1[length1]
                length1 -= 1
                length -= 1
            else:
                nums1[length] = nums2[length2]
                length2 -= 1
                length -= 1

        while length2 >= 0:
            nums1[length] = nums2[length2]
            length -= 1
            length2 -= 1

        return nums1

if __name__ == '__main__':
    s = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(s.merge(nums1, m, nums2, n))
