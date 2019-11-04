# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-03 12:01
# @Author   : Fabrice LI
# @File     : 20191102_15_permutations.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a list of numbers, return all possible permutations.
#Reference:**********************************************
'''
E.g
Input: [1]
Output:
[
  [1]
]

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Challenge
Do it without recursion.
'''


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return []
        used = [False] * len(nums)
        print(used)
        res = []
        self.dfs(nums, 0, [], used, res)
        return res

    def dfs(self, nums, index, path, used, res):
        if index == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, index + 1, path, used, res)
                used[i] = False
                path.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
