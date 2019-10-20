# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-07 00:36
# @Author   : Fabrice LI
# @File     : 480_binary_tree_paths.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return all root-to-leaf paths.
#Reference:**********************************************
'''
E.g
Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5

Input：{1,2}
Output：["1->2"]
Explanation：
   1
 /
2

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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        if not root.left and not root.right:
            res.append(str(root.val))

        left = self.binaryTreePaths(root.left)
        for l in left:
            res.append(str(root.val) + '->' + l)

        right = self.binaryTreePaths(root.right)
        for r in right:
            res.append(str(root.val) + '->' + r)
        return res
