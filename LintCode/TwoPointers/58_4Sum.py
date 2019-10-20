# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-01 22:42
# @Author   : Fabrice LI
# @File     : 58_4Sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an array S of n integers, are there elements a, b, c, and d
#               in S such that a + b + c + d = target?
#
#               Find all unique quadruplets in the array which gives the sum of target.
#               Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
#               The solution set must not contain duplicate quadruplets.
#Reference:**********************************************
'''
E.g
Input:[2,7,11,15],3
Output:[]

Input:[1,0,-1,0,-2,2],0
Output:
[[-1, 0, 0, 1]
,[-2, -1, 1, 2]
,[-2, 0, 0, 2]]
'''

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers:
            return []



if __name__ == '__main__':
    s = Solution()
    numbers = []
    target = 3
    print(s.fourSum(numbers, target))
