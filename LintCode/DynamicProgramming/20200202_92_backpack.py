# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-04 16:21
# @Author   : Fabrice LI
# @File     : 20200202_92_backpack.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n items with size Ai, an integer m denotes the size of a backpack.
#               How full you can fill this backpack?
#Reference:**********************************************
"""
Example 1:
	Input:  [3,4,8,5], backpack size=10
	Output:  9

Example 2:
	Input:  [2,3,5,7], backpack size=12
	Output:  12

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        size = len(A)

        # 定义状态
        dp = [[0 for _ in range(m + 1)] for _ in range(size + 1)]
        # 初始化状态方程
        dp[0][0] = 1
        for r in range(size + 1):
            dp[r][0] = 1

        for r in range(1, size + 1):
            for c in range(1, m + 1):
                dp[r][c] = dp[r - 1][c]
                if c >= A[r - 1]:
                    dp[r][c] = dp[r - 1][c - A[r - 1]] or dp[r - 1][c]

        for res in range(m, -1, -1):
            if dp[size][res]:
                return res
        return 0

    def backPack2(self, m, A):
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]

        f[0][0] = True
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]

        for i in range(m, -1, -1):
            if f[n][i]:
                return i
        return 0


if __name__ == '__main__':
    s = Solution()
    A = [828,125,740,724,983,321,773,678,841,842,875,377,674,144,340,467,625,916,463,922,255,662,692,123,778,766,254,559,480,483,904,60,305,966,872,935,626,691,832,998,508,657,215,162,858,179,869,674,452,158,520,138,847,452,764,995,600,568,92,496,533,404,186,345,304,420,181,73,547,281,374,376,454,438,553,929,140,298,451,674,91,531,685,862,446,262,477,573,627,624,814,103,294,388]
    m = 5000
    print(s.backPack(m, A))


