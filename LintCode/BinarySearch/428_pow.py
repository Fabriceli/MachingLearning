# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-17 20:17
# @Author   : Fabrice LI
# @File     : 428_pow.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Implement pow(x, n). (n is an integer.)
# Reference:**********************************************
'''
E.g
Input: x = 9.88023, n = 3
Output: 964.498

Input: x = 2.1, n = 3
Output: 9.261

Input: x = 1, n = 0
Output: 1

Challenge
O(logn) time
'''


class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):
        if x == 0:
            return 0
        if x == 1 or n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        r = 1
        while n:
            if n & 1:
                r = r * x
            x = x * x
            n >>= 1
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(9.88023, 3))
