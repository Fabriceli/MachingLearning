# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-17 00:05
# @Author   : Fabrice LI
# @File     : 97_maximum_depth_of_binary_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, find its maximum depth.
#
#               The maximum depth is the number of nodes along
#               the longest path from the root node down to the farthest leaf node.
#Reference:**********************************************
'''
E.g
Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.

Input: tree = {1,2,3,#,#,4,5}
Output: 3
Explanation: Like this:
   1
  / \
 2   3
    / \
   4   5
it will be serialized {1,2,3,#,#,4,5}
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        if not root:
            return 0

        m1 = self.maxDepth(root.left)
        m2 = self.maxDepth(root.right)
        return max(m1, m2) + 1
