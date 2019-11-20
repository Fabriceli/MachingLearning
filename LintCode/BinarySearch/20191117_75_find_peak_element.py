# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-17 22:19
# @Author   : Fabrice LI
# @File     : 20191117_75_find_peak_element.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There is an integer array which has the following features:
#
#               The numbers in adjacent positions are different.
#               A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
#               We define a position P is a peak if:
#
#               A[P] > A[P-1] && A[P] > A[P+1]
#
#               Find a peak element in this array. Return the index of the peak.
#
#               - It's guaranteed the array has at least one peak.
#               - The array may contain multiple peeks, find any of them.
#               - The array has at least 3 numbers in it.
#Reference:**********************************************
'''
E.g
Input:  [1, 2, 1, 3, 4, 5, 7, 6]
Output:  1 or 6

Explanation:
return the index of peek.

Input: [1,2,3,4,1]
Output:  3

Challenge
Time complexity O(logN)
'''
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        if len(A) <= 0:
            return -1
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if A[mid - 1] > A[mid]:
                right = mid
            elif A[mid] < A[mid + 1]:
                left = mid
            else:
                right = mid

        if A[right] > A[left]:
            return right
        else:
            return left


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    print(s.findPeak(nums))
