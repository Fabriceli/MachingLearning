# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-19 21:31
# @Author   : Fabrice LI
# @File     : 20191119_28_search_a_2D_matrix.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Write an efficient algorithm that searches for a value in an m x n matrix.
#               This matrix has the following properties:
#
#               Integers in each row are sorted from left to right.
#               The first integer of each row is greater than the last integer of the previous row.
#Reference:**********************************************
"""
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row <= 0:
            return False
        column = len(matrix[0])
        if column <= 0:
            return False
        left = 0
        right = row * column - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            c = int(mid / column)
            r = int(mid % column)
            if matrix[c][r] == target:
                return True
            elif matrix[c][r] > target:
                right = mid
            elif matrix[c][r] < target:
                left = mid
        c = int(left / column)
        r = int(left % column)
        if matrix[c][r] == target:
            return True
        c = int(right / column)
        r = int(right % column)
        if matrix[c][r] == target:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[]]
    target = 23
    print(s.searchMatrix(matrix, target))
