# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-10 23:06
# @Author   : Fabrice LI
# @File     : 20200208_655_add_strings.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#Reference:**********************************************
"""
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input : num1 = "123", num2 = "45"
Output : "168"
"""
# 逐位加法，注意进位
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        size1, size2, carry = len(num1), len(num2), 0
        size_max = max(size1, size2)
        res = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(size_max):
            a = int(num1[i]) if i < size1 else 0
            b = int(num2[i]) if i < size2 else 0
            temp = a + b + carry
            carry = temp // 10
            temp = temp % 10
            res += str(temp)
        return res[::-1] if not carry else '1' + res[::-1]


if __name__ == '__main__':
    s = Solution()
    num1 = '123'
    num2 = '45'
    print(s.addStrings(num1, num2))
