# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-20 20:17
# @Author   : Fabrice LI
# @File     : 61_search_for_a_range.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given a sorted array of n integers, find the starting and ending position of a given target value.
#               If the target is not found in the array, return [-1, -1].
#Reference:**********************************************
'''
E.g
Input:
[]
9
Output: [-1,-1]

Input:
[5, 7, 7, 8, 8, 10]
8
Output: [3, 4]

Challenge
O(log n) time.
'''

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        left = 0
        right = len(A) # 注意
        # [left, right)左闭右开
        res = []
        # 先找左边界
        while left < right:
            mid = (right + left) >> 1
            if A[mid] < target:
                left = mid + 1
            elif A[mid] >= target: # 注意 =：是逼近条件，不断向左逼近
                right = mid
        res.append(right if A[right] == target else -1)

        # 查找right边界
        l = 0
        h = len(A) # 注意
        while l < h:
            mid = (h + l) >> 1
            if A[mid] <= target: # 不断向右逼近
                l = mid + 1 # 注意，加1了，后面取res时候需要减1
            elif A[mid] > target:
                h = mid
        if l not in res:
            res.append(h - 1 if A[h - 1] == target else -1)
        return res

    def searchRangeComm(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        res = []
        # first index
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            res.append(left)
        if nums[right] == target:
            res.append(right)

        # last index
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[right] == target:
            res.append(right)
        if nums[left] == target:
            res.append(left)
        return res if res else [-1, -1]


if __name__ == '__main__':
    s = Solution()
    A = [-1,0,1,2,2,2,3,3,3,4,4,4,5,5,6,90,92,93,101]
    target = 2
    print(s.searchRangeComm(A, target))
