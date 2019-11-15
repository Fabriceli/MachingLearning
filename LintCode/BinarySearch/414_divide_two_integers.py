# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-19 12:24
# @Author   : Fabrice LI
# @File     : 414_divide_two_integers.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Divide two integers without using multiplication, division and mod operator.
#               If it will overflow(exceeding 32-bit signed integer representation range), return 2147483647
#               The integer division should truncate toward zero.
#Reference:**********************************************
'''
E.g
Input: dividend = 0, divisor = 1
Output: 0

Input: dividend = 100, divisor = 9
Output: 11

Input: dividend = 7, divisor = -3
Output: -2
'''


class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        sign = dividend ^ divisor
        res = 0
        count = 1
        a = abs(dividend)
        b = abs(divisor)
        while a >= b or count > 1:
            if a >= b:
                res += count
                a -= b
                b += b
                count += count
            else:
                count >>= 1
                b >>= 1
        res = res if sign >= 0 else -res
        return max(min(res, 2**31 - 1), -2**31)


if __name__ == '__main__':
    s = Solution()
    dividend = 1
    divisor = 1
    print(s.divide(dividend, divisor))
