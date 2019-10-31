# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-30 19:49
# @Author   : Fabrice LI
# @File     : 20191030_152_combinations.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two integers n and k. Return all possible combinations of k numbers out of 1, 2, ... , n
#               You can return all combinations in any order, but numbers in a combination should be in ascending order.
#Reference:**********************************************
'''
E.g
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Input: n = 4, k = 1
Output: [[1],[2],[3],[4]]
'''

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        if n <= 0 or k > n or k <= 0:
            return [[]]

        res = []
        self.dfs(n, 1, [], k, res)
        return res

    def dfs(self, n, begin, path, k, res):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(begin, n + 2 - k + len(path)):
            path.append(i)
            self.dfs(n, i + 1, path, k, res)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n, k))

