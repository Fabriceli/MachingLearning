# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-29 19:20
# @Author   : Fabrice LI
# @File     : 59_3sum_closest.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an array S of n integers, find three integers in
#               S such that the sum is closest to a given number, target.
#               Return the sum of the three integers.
#               You may assume that each input would have exactly one solution.
#Reference:**********************************************
'''
E.g
Input:[2,7,11,15],3
Output:20
Explanation:
2+7+11=20

Input:[-1,2,1,-4],1
Output:2
Explanation:
-1+2+1=2

Challenge
O(n^2) time, O(1) extra space
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3:
            return 0
        length = len(numbers)
        numbers.sort()
        sum = numbers[0] + numbers[1] + numbers[2]
        for i in range(length - 2):
            left = i + 1
            right = length - 1
            while left < right:
                temp_sum = numbers[i] + numbers[left] + numbers[right]
                if abs(sum - target) > abs(temp_sum - target):
                    sum = temp_sum
                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left += 1
                elif temp_sum == target:
                    return temp_sum
        return sum


if __name__ == '__main__':
    s = Solution()
    numbers = [0,2,1,-3]
    target = 1
    print(s.threeSumClosest(numbers, target))
