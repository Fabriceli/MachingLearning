# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-15 22:27
# @Author   : Fabrice LI
# @File     : 20200114_191_maximum_product_subarray.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Find the contiguous subarray within an array (containing at least one number)
#               which has the largest product.
#Reference:**********************************************
"""
Input:[2,3,-2,4]
Output:6

Input:[-1,2,4,1]
Output:8
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        dp_max = [1 for _ in range(size)]
        dp_min = [1 for _ in range(size)]
        result = 0
        for i in range(size):
            dp_max[i] = nums[i]
            if i > 0:
                dp_max[i] = max(nums[i], max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]))
            dp_min[i] = nums[i]
            if i > 0:
                dp_min[i] = min(nums[i], min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]))

            result = max(dp_min[i], dp_max[i], result)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-1,2,4,1]
    print(s.maxProduct(nums))

