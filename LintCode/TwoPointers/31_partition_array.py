# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-26 12:01
# @Author   : Fabrice LI
# @File     : 31_partition_array.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array nums of integers and an int k,
#               partition the array (i.e move the elements in "nums") such that:
#
#               - All elements < k are moved to the left
#               - All elements >= k are moved to the right
#               Return the partitioning index, i.e the first index i nums[i] >= k.
#
#               You should do really partition in array nums instead of just counting
#               the numbers of integers smaller than k.
#               If all elements in nums are smaller than k, then return nums.length
#Reference:**********************************************
'''
E.g
Input:
[],9
Output:
0

Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1

Challenge
Can you partition the array in-place and in O(n)?
'''

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0

        pass


if __name__ == '__main__':
    s = Solution()
    nums = []
    k = 2
    print(s.partitionArray(nums, k))
