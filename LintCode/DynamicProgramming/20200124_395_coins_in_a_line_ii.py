# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-27 15:23
# @Author   : Fabrice LI
# @File     : 20200124_395_coins_in_a_line_ii.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are n coins with different value in a line. Two players take turns to take one or two coins from
#               left side until there are no more coins left. The player who take the coins with the most value wins.
#
#               Could you please decide the first player will win or lose?
#
#               If the first player wins, return true, otherwise return false.
#Reference:**********************************************
"""
Input: [1, 2, 2]
Output: true
Explanation: The first player takes 2 coins.

Input: [1, 2, 4]
Output: false
Explanation: Whether the first player takes 1 coin or 2, the second player will gain more value.


"""
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        if not values:
            return False
        size = len(values)
        # dp[i]表示剩余i个硬币时，先手最后能取到硬币的最大价值
        dp = [0 for _ in range(size + 1)]
        values_sum = sum(values)

        for i in range(size + 1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = values[-1]
            elif i == 2:
                dp[i] = values[-1] + values[-2]
            elif i == 3:
                dp[i] = values[-2] + values[-3]
            else:
                # left表示先手拿了一个后，后手拿了一个或者两个后的，留给先手最少的价值
                left = min(dp[i - 2], dp[i - 3])
                # right表示先手拿了两个后，后手拿了一个或者两个后，留给先手最少的价值
                right = min(dp[i - 3], dp[i - 4])
                # 先手拿到左右两个分支中最大的价值，要加上先手拿了一个的价值和拿了两个的价值，再取最大值
                dp[i] = max(left + values[-i], right + values[-i] + values[-i + 1])
        return 2 * dp[size] > values_sum


if __name__ == '__main__':
    s = Solution()
    values = [5, 1, 2, 10, 7, 8]
    print(s.firstWillWin(values))

