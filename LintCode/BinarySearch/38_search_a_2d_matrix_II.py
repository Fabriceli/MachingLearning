# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-21 16:31
# @Author   : Fabrice LI
# @File     : 38_search_a_2d_matrix_II.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.
#
#               This matrix has the following properties:
#
#                   - Integers in each row are sorted from left to right.
#                   - Integers in each column are sorted from up to bottom.
#                   - No duplicate integers in each row or column.
# Reference:**********************************************
'''
E.g
Input:
	[[3,4]]
	target=3
Output:1

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2

Challenge
O(m+n) time and O(1) extra space
'''


class Solution(object):
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        res = 0
        for nums in matrix:
            res += self.search(nums, target)
        return res

    def search(self, nums, target):
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        res = 0
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                res = 1
                return res
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return res


    # 优化方案，另外一个条件没有使用：纵列也是由大到小
    def searchMatrixF(self, matrix, target):
        if not matrix:
            return False
        x = 0
        y = len(matrix[0]) - 1
        while x <= len(matrix) - 1 and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 3, 5, 7],
              [2, 4, 7, 8],
              [3, 5, 9, 10]]
    target = 11
    print(s.searchMatrixF(matrix, target))
