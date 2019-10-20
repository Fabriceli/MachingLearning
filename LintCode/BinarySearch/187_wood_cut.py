# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-23 18:53
# @Author   : Fabrice LI
# @File     : 187_wood_cut.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given n pieces of wood with length L[i] (integer array).
#               Cut them into small pieces to guarantee you could have equal or
#               more than k pieces with the same length. What is the longest length
#               you can get from the n pieces of wood? Given L & k,
#               return the maximum length of the small pieces.
#
#               You couldn't cut wood into float length.
#               If you couldn't get >= k pieces, return 0.
#Reference:**********************************************
'''
E.g

Input:
L = [232, 124, 456]
k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114cm long,
however we can't cut it into 7 pieces if any piece is 115cm long.

Input:
L = [1, 2, 3]
k = 7
Output: 0
Explanation: It is obvious we can't make it.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        pass


if __name__ == '__main__':
    s = Solution()
    L = [1, 2, 3]
    k = 7
    print(s.woodCut(L, k))
