# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-11-11 00:04
# @Author   : Fabrice LI
# @File     : 20191110_51_previous_permutation.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a list of integers, which denote a permutation.
#
#               Find the previous permutation in ascending order.
#               The list may contains duplicate integers.
# Reference:**********************************************
'''
E.g
Input:[1]
Output:[1]

Input:[1,3,2,3]
Output:[1,2,3,3]

Input:[1,2,3,4]
Output:[4,3,2,1]
'''


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        first_index = -1
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                first_index = i
                break
        print(first_index)

        def reverse(numbers, start, end):
            while start < end:
                numbers[start], numbers[end] = numbers[end], numbers[start]
                start += 1
                end -= 1

        if first_index == -1:
            reverse(nums, 0, length - 1)
            return nums

        second_index = -1
        for j in range(first_index + 1, length):
            if nums[j] > nums[first_index]:
                second_index = j
                break
        print(second_index)
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(nums, first_index + 1, length - 1)
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [4, 0, 7, 1, 2, 3, 8, 9]
    # nums = [1,2,3,3]
    print(s.previousPermuation(nums))
