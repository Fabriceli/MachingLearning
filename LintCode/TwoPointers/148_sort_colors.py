# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-09-28 23:29
# @Author   : Fabrice LI
# @File     : 148_sort_colors.py
# @User     : liyihao
# @Software: PyCharm
# @Description: Given an array with n objects colored red, white or blue,
#               sort them so that objects of the same color are adjacent,
#               with the colors in the order red, white and blue.
#
#               Here, we will use the integers 0, 1, and 2 to represent
#               the color red, white, and blue respectively.
#               You are not suppose to use the library's sort function for this problem.
#               You should do it in-place (sort numbers in the original array).
#Reference:**********************************************
'''
E.g
Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

'''
三指针问题：左指针，右指针，当前位置指针
1. 遇到0放在数组前面，
2. 遇到1 curr前移，
3. 遇到2放到数组后面
'''
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []
        left = curr = 0
        right = len(nums) - 1
        while curr <= right:
            if nums[curr] == 1:
                curr += 1
            elif nums[curr] == 0:
                if curr != left:
                    nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                if curr != right:
                    nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(s.sortColors(nums))
