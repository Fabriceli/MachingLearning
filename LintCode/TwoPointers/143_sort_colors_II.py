# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-25 12:27
# @Author   : Fabrice LI
# @File     : 143_sort_colors_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array of n objects with k different colors (numbered from 1 to k),
#               sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
#               1. You are not suppose to use the library's sort function for this problem.
#               2. k <= n
#Reference:**********************************************
'''
E.g
Input:
[3,2,2,1,4]
4
Output:
[1,2,2,3,4]

Input:
[2,1,1,2,2]
2
Output:
[1,1,2,2,2]

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
That will cost O(k) extra memory. Can you do it without using extra memory?
'''


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if not colors:
            return []
        start = 0
        end = len(colors) - 1

        pass

if __name__ == '__main__':
    s = Solution()
    colors = []
    k = 4
    print(s.sortColors2(colors, k))
