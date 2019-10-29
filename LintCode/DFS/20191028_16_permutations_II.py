# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-29 11:22
# @Author   : Fabrice LI
# @File     : 20191028_16_permutations_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a list of numbers with duplicate number in it. Find all unique permutations.
#Reference:**********************************************
'''
E.g
Input: [1,1]
Output:
[
  [1,1]
]

Input: [1,2,2]
Output:
[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]

Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!
'''
import sys
sys.setrecursionlimit(1000000)

class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if not nums:
            return [[]]
        res = []
        nums.sort()
        used = [False] * len(nums)
        print(used)
        self.dfs(nums, 0, used, [], res)
        return res

    def dfs(self, nums, begin, used, path, res):
        if begin == len(nums):
            res.append(path.copy())
            return
        for index in range(len(nums)):
            if not used[index]:
                if index > 0 and nums[index] == nums[index - 1] and not used[index - 1]:
                    continue
                used[index] = True
                path.append(nums[index])
                self.dfs(nums, begin + 1, used, path, res)
                used[index] = False
                path.pop()

    def permuteUnique_(self, nums):
        if len(nums) == 0:
            return []

        nums.sort()
        used = [False] * len(nums)
        res = []
        self.__dfs(nums, 0, [], used, res)
        return res
    def __dfs(self, nums, index, pre, used, res):
        if index == len(nums):
            res.append(pre.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self.__dfs(nums, index + 1, pre, used, res)
                used[i] = False
                pre.pop()



if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))
