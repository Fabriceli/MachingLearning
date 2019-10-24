# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-24 21:38
# @Author   : Fabrice LI
# @File     : 20191024_94_binary_tree_maximum_path_sum.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, find the maximum path sum.
#
#               The path may start and end at any node in the tree.
#Reference:**********************************************
'''
Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2

Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3

	Output: 6
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
    def maxPathSum(self, root):
        if not root:
            return 0
        res = float('-inf')
        def maxPath(node):
            nonlocal res
            if not node:
                return 0
            left = max(maxPath(node.left), 0)
            right = max(maxPath(node.right), 0)
            path = left + right + node.val
            res = max(res, path)
            return node.val + max(left, right)
        maxPath(root)
        return res
