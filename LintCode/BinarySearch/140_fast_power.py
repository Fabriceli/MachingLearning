# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-17 10:55
# @Author   : Fabrice LI
# @File     : 140_fast_power.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Calculate the a^n % b where a, b and n are all 32bit non-negative integers.
# Reference:**********************************************
'''
Example
For 2^31 % 3 = 2
For 100^1000 % 1000 = 0

Challenge
O(logn)
'''


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # a^n%b
        if a == 1:
            return a % b
        if n == 0:
            return 1 % b
        r = 1
        while n:
            if n & 1:
                r = (r * a) % b
            a = a * a % b
            n >>= 1
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.fastPower(2, 3, 16))
