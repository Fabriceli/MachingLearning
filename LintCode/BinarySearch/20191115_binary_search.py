# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-15 11:14
# @Author   : Fabrice LI
# @File     : 20191115_binary_search.py
# @User     : liyihao
# @Software : PyCharm
# @Description: default module binary search
#Reference:**********************************************

class Solution():
    def binary_search_default(self, nums, target):
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1

    def binary_search_left_edge(self, nums, target):
        if len(nums) <= 0:
            return -1
        left = 0
        # 重点
        right = len(nums) - 1
        # 重点
        while left + 1 < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def binary_search_right_edge(self, nums, target):
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    target = 2
    print("left edge: " + str(s.binary_search_left_edge(nums, target)))
    print("right edge: " + str(s.binary_search_right_edge(nums, target)))
