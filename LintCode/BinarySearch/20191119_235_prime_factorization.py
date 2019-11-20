# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-19 20:10
# @Author   : Fabrice LI
# @File     : 20191119_235_prime_factorization.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Prime factorize a given integer.
#Reference:**********************************************
"""
Input: 10
Output: [2, 5]

Input: 660
Output: [2, 2, 3, 5, 11]

Notice
You should sort the factors in ascending order.
"""

class Solution:
    def primeFacto(self, num):
        if num <= 0:
            return []
        if num <= 2:
            return [num]
        res = []
        for i in range(2, num):
            while num % i == 0:
                res.append(i)
                num /= i
        return res


if __name__ == '__main__':
    s = Solution()
    num = 660
    print(s.primeFacto(num))
