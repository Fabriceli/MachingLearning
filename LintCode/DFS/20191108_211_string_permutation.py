# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-09 15:02
# @Author   : Fabrice LI
# @File     : 20191108_211_string_permutation.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two strings, write a method to decide if one is a permutation of the other.
#Reference:**********************************************
'''
E.g
Example 1:
	Input:  "abcd", "bcad"
	Output:  True

Example 2:
	Input: "aac", "abc"
	Output:  False
'''
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if not A or not B:
            return False
        b_list = []
        a_list = []
        for b in B:
            b_list.append(b)
        b_list.sort()
        for a in A:
            a_list.append(a)
        a_list.sort()
        for a, b in zip(a_list, b_list):
            if a != b:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    A = 'abcd'
    B = 'bcad'
    print(s.Permutation(A, B))

