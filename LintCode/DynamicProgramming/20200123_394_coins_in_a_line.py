# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-27 12:08
# @Author   : Fabrice LI
# @File     : 20200123_394_coins_in_a_line.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are n coins in a line. Two players take turns to take one or two coins from right side until
#               there are no more coins left. The player who take the last coin wins.
#
#               Could you please decide the first player will win or lose?
#
#               If the first player wins, return true, otherwise return false.
#Reference:**********************************************
"""
Input: 1
Output: true

Input: 4
Output: true
Explanation:
The first player takes 1 coin at first. Then there are 3 coins left.
Whether the second player takes 1 coin or two, then the first player can take all coin(s) left.

Challenge
O(n) time and O(1) memory
"""
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if not n:
            return False
        dp = [False for _ in range(n + 1)]

        for i in range(n + 1):
            if i == 0 or i == 3:
                dp[i] = False
            elif i == 1 or i == 2:
                dp[i] = True
            else:
                dp[i] = (dp[i - 2] and dp[i - 3]) or (dp[i - 3] and dp[i - 4])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    n = 12
    print(s.firstWillWin(n))
