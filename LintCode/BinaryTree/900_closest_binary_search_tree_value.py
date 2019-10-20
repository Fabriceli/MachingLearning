# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-05 01:28
# @Author   : Fabrice LI
# @File     : 900_closest_binary_search_tree_value.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a non-empty binary search tree and a target value,
#               find the value in the BST that is closest to the target.
#               Given target value is a floating point.
#               You are guaranteed to have only one unique value in the BST that is closest to the target.
#Reference:**********************************************
'''
E.g
Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return -1
        res = root.val
        if res > target and root.left:
            val = self.closestValue(root.left, target)
        elif res < target and root.right:
            val = self.closestValue(root.right, target)
        else:
            return res
        if abs(res - target) > abs(val - target):
            res = val
        return res


if __name__ == '__main__':
    s = Solution()
    root = {}
    target = 4.142857
    print(s.closestValue(root, target))
