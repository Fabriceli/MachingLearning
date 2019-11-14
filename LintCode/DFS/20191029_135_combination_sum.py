# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-29 11:22
# @Author   : Fabrice LI
# @File     : 20191029_135_combination_sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a set of candidtate numbers candidates and a target number target.
#               Find all unique combinations in candidates where the numbers sums to target.
#
#               The same repeated number may be chosen from candidates unlimited number of times.
#               1. All numbers (including target) will be positive integers.
#               2. Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
#               3. Different combinations can be in any order.
#               4. The solution set must not contain duplicate combinations.
#Reference:**********************************************
'''
E.g
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]

Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
'''

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        res = []
        candidates.sort()
        self.dfs(candidates, 0, len(candidates), [], res, target)
        return res

    def dfs(self, data, begin, size, path, res, target):
        if target == 0:
            if path not in res:
                res.append(path[:])
            return
        for index in range(begin, size):
            reduce = target - data[index]
            if reduce < 0:
                break
            path.append(data[index])
            self.dfs(data, index, size, path, res, reduce)
            path.pop()


    def combinationSum2(self, candidates, target):
        if len(candidates) <= 0:
            return []
        res = []
        candidates.sort()
        self.__dfs(candidates, target, 0, [], res)
        return res

    # 递归的定义
    # 找到所有以condidate开头的的哪些和为target的结果都放到res里，下一个加入path的数，
    # 至少从candidate的start_index开始
    def __dfs(self, candidates, remain_target, start_index, path, res):
        if remain_target == 0:
            res.append(path[:])
            return
        # 递归的拆解
        for i in range(start_index, len(candidates)):
            if remain_target < candidates[i]:
                break
            # 去掉candidate中重复的，[2，2，3，4，6]
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.__dfs(candidates, remain_target - candidates[i], i, path, res)
            path.pop()



if __name__ == '__main__':
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(s.combinationSum2(candidates, target))
