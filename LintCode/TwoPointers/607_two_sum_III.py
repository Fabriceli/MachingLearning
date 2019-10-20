# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-23 19:34
# @Author   : Fabrice LI
# @File     : 607_two_sum_III.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Design and implement a TwoSum class. It should support the following operations: add and find.
#               add - Add the number to an internal data structure.
#               find - Find if there exists any pair of numbers which sum is equal to the value.
#Reference:**********************************************
'''
E.g
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.nums = []
    def add(self, number):
        # write your code here
        self.nums.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        if not self.nums:
            return False
        left = 0
        right = len(self.nums) - 1
        self.nums.sort()
        while left < right:
            sum = self.nums[left] + self.nums[right]
            if sum == value:
                return True
            elif sum > value:
                right -= 1
                while left < right and self.nums[right] == self.nums[right + 1]:
                    right -= 1
            elif sum < value:
                left += 1
                while left < right and self.nums[left] == self.nums[left - 1]:
                    left += 1
        return False


if __name__ == '__main__':
    s = TwoSum()
    s.add(1)
    s.add(3)
    s.add(5)
    print(s.find(4))
    print(s.find(7))
