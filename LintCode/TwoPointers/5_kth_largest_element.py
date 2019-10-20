# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-26 18:34
# @Author   : Fabrice LI
# @File     : 5_kth_largest_element.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Find K-th largest element in an array.
#               You can swap elements in the array
#Reference:**********************************************
'''
E.g
Input:
n = 1, nums = [1,3,4,2]
Output:
4

Input:
n = 3, nums = [9,3,2,4,8]
Output:
4

Challenge
O(n) time, O(1) extra memory.
'''

import heapq

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums:
            return 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(n):
            res = heapq.heappop(nums)
        return -res


if __name__ == '__main__':
    s = Solution()
    n = 1
    nums = [1,3,4,2]
    print(s.kthLargestElement(n, nums))
