# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-11 00:10
# @Author   : Fabrice LI
# @File     : 20191111_52_next_permutation.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Implement next permutation, which rearranges numbers into the lexicographically
#               next greater permutation of numbers.
#
#               If such arrangement is not possible, it must rearrange it as the lowest possible order
#               (ie, sorted in ascending order).
#
#               The replacement must be in-place and use only constant extra memory.
#
#               Here are some examples. Inputs are in the left-hand column and its corresponding
#               outputs are in the right-hand column.
#Reference:**********************************************
'''
E.g
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution:
    def nextPermutation(self, nums):
        if not nums:
            return []
        first_index = -1
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break

        def reverse(numbers, start, end):
            while end > start:
                numbers[end], numbers[start] = numbers[start], numbers[end]
                end -= 1
                start += 1

        if first_index == -1:
            reverse(nums, 0, length - 1)
            return nums

        second_index = -1
        for j in range(length - 1, first_index, -1):
            if nums[j] > nums[first_index]:
                second_index = j
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(nums, first_index + 1, length - 1)
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, 2]
    print(s.nextPermutation(nums))
