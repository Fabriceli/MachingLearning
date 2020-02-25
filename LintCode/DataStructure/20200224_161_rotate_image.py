# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-02-24 23:54
# @Author   : Fabrice LI
# @File     : 20200224_161_rotate_image.py
# @User     : liyihao
# @Software : PyCharm
# @Description: You are given an n x n 2D matrix representing an image.
#               Rotate the image by 90 degrees (clockwise).
#Reference:**********************************************
"""
Input:[[1,2],[3,4]]
Output:[[3,1],[4,2]]

Input:[[1,2,3],[4,5,6],[7,8,9]]
Output:[[7,4,1],[8,5,2],[9,6,3]]

Challenge
Do it in-place.
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - 1 - i): # (n - i - 1) + i if n & 1 else (n - 2 * i - 1) + i
                matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                    matrix[n - 1 - j][i], matrix[i][j], matrix[j][n - 1 - i], matrix[n - 1 - i][n - 1 - j]



if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
