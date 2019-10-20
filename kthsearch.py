# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-09-02 00:24
# @Author   : Fabrice LI
# @File     : kthsearch.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Find the kth largest element in an unsorted array.
#               Note that it is the kth largest element in the sorted order,
#               not the kth distinct element.
# Reference:**********************************************

import heapq
import math
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = 0
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        res = 0
        for _ in range(k):
            res = heapq._heappop_max(nums)
        return res

    def is_prime(self, number):
        if number <= 1:
            return False
        else:
            for i in range(2, number if int(number / 2) <= 2 else int(number / 2)):
                if number % i == 0:
                    return False
            return True

    def find_prime_number(self, n: int):
        if n <= 1:
            return
        nums = 0
        for i in range(2, n + 1):
            if self.is_prime(i):
                nums = nums + 1
        return nums

    def cal_nums(self, number):
        if number < 0:
            return
        res = 1
        for i in range(1, number+1):
            res = res * i
        return res

    def dietPlanPerformance(self, calories, k, lower, upper):
        if not calories:
            return
        l = len(calories)
        res = 0
        for j in range(l):
            t = 0
            if (j + k) >= l:
                return res
            for i in range(j, k + j):
                t = calories[i] + t
            if t < lower:
                res = res - 1
            elif t > upper:
                res = res + 1
        return res

    def dietPlanPerformance2(self, calories, k, lower, upper):
        if not calories:
            return
        l = len(calories)
        res = 0
        sum = 0
        for i in range(l):
            sum = calories[i] + sum
            if i >= k:
                sum -= calories[i - k]
                pass
            if i >= (k - 1):
                if sum < lower:
                    res -= 1
                elif sum > upper:
                    res += 1
        return res

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        carry = 0
        temp = 0
        while not l1 or not l2 or not carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            res.val = (a + b + carry) % 10
            carry = (a + b) // 10
            res = res.next
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
        return res





if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    print(solution.findKthLargest(nums, 2))
    print(solution.findKthLargest2(nums, 2))
    n = 100
    a = solution.find_prime_number(n)
    b = n - a
    c = math.factorial(b)
    d = math.factorial(a)
    pow()
    print((c * d) % (10^9 + 7))
