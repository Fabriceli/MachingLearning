# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-27 22:55
# @Author   : Fabrice LI
# @File     : 382_triangle_count.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array of integers, how many three numbers can be found in the array,
#               so that we can build an triangle whose three edges length is the three numbers that we find?
#Reference:**********************************************
'''
E.g
Input: [3, 4, 6, 7]
Output: 3
Explanation:
They are (3, 4, 6),
         (3, 6, 7),
         (4, 6, 7)

Input: [4, 4, 4, 4]
Output: 4
Explanation:
Any three numbers can form a triangle.
So the answer is C(3, 4) = 4
'''
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S:
            return 0
        length = len(S)
        S.sort()
        res = 0
        for i in range(length - 1, -1, -1):
            left = 0
            right = i - 1
            while left < right:
                if S[right] + S[left] > S[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    S = [4, 4, 4, 4]
    print(s.triangleCount(S))
