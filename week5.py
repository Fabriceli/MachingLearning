# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-08-27 00:05
# @Author   : Fabrice LI
# @File     : week5.py
# @User     : liyihao
# @Software: PyCharm
# @Description: todo
# Reference:**********************************************

"""
sqrt binary search
"""
from decimal import Decimal
from typing import List
import sys

sys.setrecursionlimit(99999999)


def cal_sqrt(x):
    if x <= 1:
        return x
    low = 1
    high = int(x / 2)
    while low <= high:
        mid = int((high + low) / 2)
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            if (mid + 1) * (mid + 1) > x:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return 1


# newton
# y = x^2 - a find a when y=0
def cal_sqrt2(x):
    if x <= 1:
        return x
    eps = 0.0001
    a = x
    while (a * a - x) > eps:
        a = 0.5 * (a + x / a)
    return int(a)


def get_range_sum_query(data_list, start, end):
    if not data_list:
        return 0
    length = len(data_list)
    result = [0] * length
    for i in range(0, length):
        result[i] = result[i - 1] + data_list[i]

    return result[end] - result[start - 1]


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(self.nums)
        self.result = []
        sum = 0
        for x in range(0, self.length):
            sum = sum + self.nums[x]
            self.result.append(sum)

    def sumRange(self, i: int, j: int) -> int:
        return self.result[j] - self.result[i] + self.nums[i]


def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    return Decimal((x * pow(x * x, int(n / 2))) if n & 1 else pow(x * x, int(n / 2))).quantize(Decimal("0.00000"))


def pow2(x, n):
    res = 1
    temp = x
    while n:
        if n & 1:
            res *= temp
        else:
            temp *= temp
        n >>= 1
    return res


def dfs(grid, row, column):
    if (row < 0) or row >= len(grid) or (column < 0) or column >= len(grid[0]) or grid[row][column] == '0':
        return
    grid[row][column] = '0'
    dfs(grid, row + 1, column)
    dfs(grid, row - 1, column)
    dfs(grid, row, column + 1)
    dfs(grid, row, column - 1)
    return


def get_island_num(grid):
    if not grid:
        return
    row = len(grid)
    if not row:
        return
    column = len(grid[0])
    if not column:
        return
    num = 0
    for r in range(row):
        for c in range(column):
            if grid[r][c] == '1':
                dfs(grid, r, c)
                num = num + 1
        print(grid[r])
    return num


def get_range_sum_query_2d(grid: List[List[int]], r1, c1, r2, c2):
    if not grid:
        return
    row = len(grid)
    if not row:
        return
    column = len(grid[0])
    if not column:
        return
    res = [[0] * (column + 1) for _ in range(row + 1)]
    for r in range(1, row + 1):
        for c in range(1, column + 1):
            res[r][c] = res[r - 1][c] + res[r][c - 1] - res[r - 1][c - 1] + grid[r - 1][c - 1]

    for t in res:
        print(t)
    return res[r2 + 1][c2 + 1] - res[r1][c2 + 1] - res[r2 + 1][c1] + res[r1][c1]


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not matrix:
            return
        row = len(matrix)
        if not row:
            return
        column = len(matrix[0])
        if not column:
            return
        res = [[0] * (column + 1) for _ in range(row + 1)]
        for r in range(1, row + 1):
            for c in range(1, column + 1):
                res[r][c] = res[r - 1][c] + res[r][c - 1] - res[r - 1][c - 1] + matrix[r - 1][c - 1]
        self.res = res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.res[row2 + 1][col2 + 1] + self.res[row1][col1] - self.res[row2 + 1][col1] - self.res[row1][col2 + 1]


if __name__ == '__main__':
    # print(cal_sqrt2(16))
    # data = [2, -3, 0, 4, 6, -5, 8]
    # print(data)
    # print(get_range_sum_query(data, 2, 5))
    # nums = [-2, 0, 3, -5, 2, -1]
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(0, 2)
    # param_2 = obj.sumRange(2, 5)
    # param_3 = obj.sumRange(0, 5)
    # print(param_1)
    # print(param_2)
    # print(param_3)
    # print(pow2(2, 2))
    # data = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    # for i in data:
    #     # for j in i:
    #     #     if j == "0":
    #     #         print("#####")
    #     #         continue
    #     print(i)
    # print("#"*40)
    # print(get_island_num(data))
    grid = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]]
    for j in grid:
        print(j)
    print("%%%" * 40)
    res = get_range_sum_query_2d(grid, 2, 1, 4, 3)
    print(res)
