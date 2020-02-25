# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-10 23:24
# @Author   : Fabrice LI
# @File     : 20200209_656_multiply_strings.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two non-negative integers num1 and num2 represented as strings,
#               return the product of num1 and num2
#Reference:**********************************************
"""
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Input:
"123"
"45"
Output:
"5535"
Explanation:
123 x 45 = 5535

Input:
"0"
"0"
Output:
"0"
"""

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    # 思路：竖式计算法
    # 1. 两数相乘结果的长度小于等于两数长度之和
    # 2. num1的第i个数字与num2的第j个数字相乘，结果为i+j到i+j+1的位置
    def multiply2(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        size1 = len(num1)
        size2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0 for _ in range(size1 + size2)]
        for i in range(size1):
            for j in range(size2):
                temp = int(num1[i]) * int(num2[j]) + res[i + j]
                decade = temp // 10 + res[i + j + 1]
                unit = temp % 10
                res[i + j] = unit
                res[i + j + 1] = decade
        print(res)
        return ''.join(str(num) for num in res[::-1])

    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        size1 = len(num1)
        size2 = len(num2)

        if size1 < size2:
            size1, size2 = size2, size1
            num1, num2 = num2, num1
        res = '0'
        num2 = num2[::-1]
        for i, num in enumerate(num2):
            temp = self.mup(num1, int(num)) + '0' * i
            res = self.add(res, temp)
        return res

    def mup(self, num1, num2):
        # num1 长字符串， num单字符串
        # 1234 * 5
        num1 = num1[::-1]
        # 4321 * 5
        res = []
        for i, num in enumerate(num1):
            temp = int(num) * num2
            res.append(temp)
        res = self.carry(res)
        return ''.join(str(i) for i in res[::-1])

    def carry(self, nums):
        size = len(nums)
        res = []
        carry = 0
        for i in range(size):
            a = nums[i] % 10 + carry
            carry = nums[i] // 10
            if a:
                res.append(a)
        if carry:
            res.append(carry)
        return res


    def add(self, num1, num2):
        size1 = len(num1)
        size2 = len(num2)

        size_max = max(size1, size2)
        res = ''
        carry = 0
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
    num1 = "123"
    num2 = '456'
    print(s.multiply2(num1, num2))
    # "56088"
