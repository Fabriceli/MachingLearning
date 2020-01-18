# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-15 19:51
# @Author   : Fabrice LI
# @File     : 20200115_669_coin_change.py
# @User     : liyihao
# @Software : PyCharm
# @Description: You are given coins of different denominations and a total amount of money amount.
#               Write a function to compute the fewest number of coins that you need to make up that amount.
#               If that amount of money cannot be made up by any combination of the coins, return -1.
#Reference:**********************************************
"""
Input:
[1, 2, 5]
11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input:
[2]
3
Output: -1
"""
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [MAX for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == MAX:
            return -1
        return int(dp[amount])


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(s.coinChange(coins, amount))
