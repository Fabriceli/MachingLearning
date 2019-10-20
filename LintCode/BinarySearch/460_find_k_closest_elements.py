# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-17 22:05
# @Author   : Fabrice LI
# @File     : 460_find_k_closest_elements.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given target, a non-negative integer k and an integer array A sorted in ascending order,
#               find the k closest numbers to target in A, sorted in ascending order by the difference
#               between the number and target. Otherwise, sorted in ascending order by number if the
#               difference is same.
#Reference:**********************************************
'''
E.g
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]

Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]

Challenge
O(logn + k) time
'''

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, nums, target, k):
        if not nums:
            return []
        left = 0
        right = len(nums) - k
        while left < right:
            mid = (left + right) >> 1
            if target > nums[mid]:
                if target - nums[mid] > nums[mid + k] - target:
                    left = mid + 1
                else:
                    right = mid
            else:
                right = mid
        return left


    # for lintcode res has order
    def kClosestNumbersNor(self, nums, target, k):
        if not nums:
            return []
        index = self.binary_search(nums, target)
        res = []
        left = index
        right = index + 1
        while k:
            if left < 0:
                res.append(nums[right])
                right += 1
                k -= 1
            elif right > len(nums) - 1:
                res.append(nums[left])
                left -= 1
                k -= 1
            elif abs(target - nums[left]) <= abs(target - nums[right]):
                res.append(nums[left])
                left -= 1
                k -= 1
            else:
                res.append(nums[right])
                right += 1
                k -= 1
        return res


    def binary_search(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return left if abs(target - nums[left]) <= abs(target - nums[right]) else right


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,4,5,6,7,8,10]
    k = 0
    target = 5
    print(s.kClosestNumbers(nums, target, k))
    print(s.kClosestNumbersNor(nums, target, k))
