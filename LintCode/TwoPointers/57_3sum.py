# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-26 00:41
# @Author   : Fabrice LI
# @File     : 57_3sum.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
#               Find all unique triplets in the array which gives the sum of zero.
#               1. Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#               2. The solution set must not contain duplicate triplets.
#Reference:**********************************************
'''
E.g
Input:[2,7,11,15]
Output:[]

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers:
            return []
        numbers.sort()
        res = []
        length = len(numbers)
        for start in range(length):
            if numbers[start] > 0:
                return res
            if start > 0 and numbers[start] == numbers[start - 1]:
                continue
            left = start + 1
            right = length - 1
            while left < right:
                sum = numbers[start] + numbers[left] + numbers[right]
                if sum == 0:
                    res.append([numbers[start], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    numbers = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(s.threeSum(numbers))
