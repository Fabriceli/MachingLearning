# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-04 22:57
# @Author   : Fabrice LI
# @File     : 20200204_125_backpack_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are n items and a backpack with size m. Given array A representing the size of each item and
#               array V representing the value of each item.
#
#               What's the maximum value can you put into the backpack?
#Reference:**********************************************
"""
- A[i], V[i], n, m are all integers.
- You can not split an item.
- The sum size of the items you want to put into backpack can not exceed m.
- Each item can only be picked up once

Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9

Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
Output: 10
Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10

Challenge
O(nm) memory is acceptable, can you do it in O(m) memory?
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        rows = len(A)
        columns = m

        # 初始化状态方程
        dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if c >= A[r - 1]:
                    dp[r][c] = max(dp[r - 1][c], dp[r - 1][c - A[r - 1]] + V[r - 1])
                else:
                    dp[r][c] = dp[r - 1][c]

        return max(dp[-1])


if __name__ == '__main__':
    s = Solution()
    m = 10
    A = [2, 3, 8]
    V = [2, 5, 8]
    print(s.backPackII(m, A, V))
