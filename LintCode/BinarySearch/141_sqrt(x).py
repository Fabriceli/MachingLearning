# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-21 23:15
# @Author   : Fabrice LI
# @File     : 141_sqrt(x).py
# @User     : liyihao
# @Software: PyCharm
# @Description: Implement int sqrt(int x).
#               Compute and return the square root of x.
# Reference:**********************************************
'''
Example 1:
	Input:  0
	Output: 0


Example 2:
	Input:  3
	Output: 1

	Explanation:
	return the largest integer y that y*y <= x.

Example 3:
	Input:  4
	Output: 2

Challenge
O(log(x))
'''


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        if x < 0:
            return -1
        if x == 0:
            return 0



if __name__ == '__main__':
    s = Solution()
    print(s.sqrt(10))
