# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-26 19:15
# @Author   : Fabrice LI
# @File     : 56_two_sum.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array of integers, find two numbers such that they add up to a specific target number.
#
#               The function twoSum should return indices of the two numbers such that they add up to the target,
#               where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
#               are zero-based.
#Reference:**********************************************
'''
E.g
Example1:
numbers=[2, 7, 11, 15], target=9
return [0, 1]
Example2:
numbers=[15, 2, 7, 3, 11], target=9
return [1, 2]

Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum_n(self, numbers, target):
        if not numbers:
            return []
        hashmap = {}
        length = len(numbers)
        for i in range(length):
            hashmap[numbers[i]] = i
        for i in range(length):
            find = target - numbers[i]
            if find in hashmap and i != hashmap[find]:
                return [i, hashmap[find]]
        return []

    def twoSum_nlogn(self, numbers, target):
        if not numbers:
            return []
        hashmap = {}
        length = len(numbers)
        for i in range(length):
            find = target - numbers[i]
            if find in hashmap and i != hashmap[find]:
                return [i, hashmap[find]]
            hashmap[numbers[i]] = i
        return []

if __name__ == '__main__':
    s = Solution()
    numbers = [3, 2,4]
    target = 6
    print(s.twoSum_nlogn(numbers, target))