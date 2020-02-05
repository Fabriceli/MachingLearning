# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-05 09:30
# @Author   : Fabrice LI
# @File     : 20200205_89_k_sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n distinct positive integers, integer k (k <= n) and a number target.
#
#               Find k numbers where sum is target. Calculate how many solutions there are?
#Reference:**********************************************
"""
Input:
List = [1,2,3,4]
k = 2
target = 5
Output: 2
Explanation: 1 + 4 = 2 + 3 = 5

Input:
List = [1,2,3,4,5]
k = 3
target = 6
Output: 1
Explanation: There is only one method. 1 + 2 + 3 = 6
"""
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # 定义三维数组的状态转移方程
        # dp[i][k][t]前i个元素取k个值的时候是组成t的个数
        dp = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(len(A) + 1)]
        for i in range(len(A) + 1):
            dp[i][0][0] = 1

        for i in range(1, len(A) + 1):
            for j in range(1, k + 1):
                for t in range(target + 1):
                    if t >= A[i - 1]:
                        dp[i][j][t] = dp[i - 1][j - 1][t - A[i - 1]] + dp[i - 1][j][t]
                    else:
                        dp[i][j][t] = dp[i - 1][j][t]

        return dp[-1][-1][-1]


if __name__ == '__main__':
    s = Solution()
    List = [1, 2, 3, 4]
    k = 2
    target = 5
    print(s.kSum(List, k, target))



