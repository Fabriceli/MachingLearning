# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-19 13:14
# @Author   : Fabrice LI
# @File     : 20200119_664_counting_bits.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
#               calculate the number of 1's in their binary representation and return them as an array.
#Reference:**********************************************
"""
Input: 5
Output: [0,1,1,2,1,2]
Explanation:
The binary representation of 0~5 is:
000
001
010
011
100
101
the count of "1" in each number is: 0,1,1,2,1,2

Input: 3
Output: [0,1,1,2]

Challenge
It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or
in any other language.
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num <= 0:
            return [num]
        # 定义状态转移方程 dp[i] = dp[i>>2] + i % 2
        # dp[i]表示i的数字含有多少个1，dp[i>>1]表示i去掉最后一位后有多少个1，也就是上一个数有多少个1，再加上去掉的那个数，
        # i%2表示去掉的那个数是否位1, 在计算机中取模会比较慢可以使用与代替，仅对于模2操作：i%2 = i&1
        dp = [0 for _ in range(num + 1)]

        for i in range(0, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp[:num + 1]


if __name__ == '__main__':
    s = Solution()
    num = 5
    print(s.countBits(num))
