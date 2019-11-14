# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-01 00:28
# @Author   : Fabrice LI
# @File     : 20191031_153_combination_sum_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an array num and a number target. Find all unique
#               combinations in num where the numbers sum to target.
#               - Each number in num can only be used once in one combination.
#               - All numbers (including target) will be positive integers.
#               - Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
#               - Different combinations can be in any order.
#               - The solution set must not contain duplicate combinations.
#Reference:**********************************************
'''
E.g

Input: num = [7,1,2,5,1,6,10], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Input: num = [1,1,1], target = 2
Output: [[1,1]]
Explanation: The solution set must not contain duplicate combinations.
'''
from typing import List
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        if not num:
            return [[]]

        res = []
        num.sort()
        self.dfs(num, 0, [], res, target)
        return res

    def dfs(self, num, begin, path, res, target):
        if target == 0 and path not in res:
            res.append(path[:])
            return

        for i in range(begin, len(num)):
            if num[i] > target:
                break
            path.append(num[i])
            self.dfs(num, i + 1, path, res, target - num[i])
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []

        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            if candidates[index] > residue:
                break

            # 剪枝的前提是数组升序排序
            if index > start and candidates[index - 1] == candidates[index]:
                # [1, 1, 2, 5, 6, 7, 10]
                # 0 号索引的 1 ，从后面 6 个元素中搜索
                # 1 号索引也是 1 ，从后面 5 个元素（是上面 6 个元素的真子集）中搜索，这种情况显然上面已经包含
                continue

            path.append(candidates[index])
            # 这里要传入 index + 1，因为当前元素不能被重复使用
            # 如果 index + 1 越界，传递到下一个方法中，什么也不执行
            self.__dfs(candidates, size, index + 1, path, residue - candidates[index], res)
            path.pop()

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) <= 0:
            return []
        res = []
        candidates.sort()
        self.dfs3(candidates, target, 0, [], res)
        return res

    # 递归定义
    def dfs3(self, candidates, remain_target, start_index, path, res):
        if remain_target == 0:
            res.append(path[:])
            return
        # 递归拆解
        for i in range(start_index, len(candidates)):
            if remain_target < candidates[i]:
                return
            # 不隔个取
            if i != start_index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.dfs3(candidates, remain_target - candidates[i], i, path, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    num = [1, 1, 1]
    target = 2
    print(s.combinationSum3(num, target))
