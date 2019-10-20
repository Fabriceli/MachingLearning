# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-22 15:26
# @Author   : Fabrice LI
# @File     : 617_maximum_average_subarray_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array with positive and negative numbers,
#               find the maximum average subarray which length should be greater or equal to given length k.
#Reference:**********************************************
'''
E.g
Input:
[1,12,-5,-6,50,3]
3
Output:
15.667
Explanation:
 (-6 + 50 + 3) / 3 = 15.667

 Input:
[5]
1
Output:
5.000
'''

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        pass


if __name__ == '__main__':
    s = Solution()
    nums = []
    k = 8
    print(s.maxAverage(nums, k))