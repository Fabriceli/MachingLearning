# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-29 11:22
# @Author   : Fabrice LI
# @File     : 20191027_17_subsets.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a set of distinct integers, return all possible subsets.
#               - Elements in a subset must be in non-descending order.
#               - The solution set must not contain duplicate subsets.
#Reference:**********************************************
'''
E.g
Input: [0]
Output:
[
  [],
  [0]
]

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Challenge
Can you do it in both recursively and iteratively?
'''

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        if not nums:
            return [[]]
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, begin, path, res):
        res.append(path[:])
        for index in range(begin, len(nums)):
            path.append(nums[index])
            self.dfs(nums, index + 1, path, res)
            path.pop()


    def subsets_nonre(self, nums):
        if not nums:
            return [[]]
        res = [[]]
        # TODO 循环求解法待完成


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 4]
    print(s.subsets_nonre(nums))
