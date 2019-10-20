# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-16 00:34
# @Author   : Fabrice LI
# @File     : 155_minimum_depth_of_binary_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, find its minimum depth.
#
#               The minimum depth is the number of nodes along the shortest path
#               from the root node down to the nearest leaf node.
#Reference:**********************************************
'''
E.g
Input: {}
Output: 0

Input:  {1,#,2,3}
Output: 3
Explanation:
	1
	 \
	  2
	 /
	3
it will be serialized {1,#,2,3}

Input:  {1,2,3,#,#,4,5}
Output: 2
Explanation:
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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)
        if not root.left or not root.right:
            return m1 + m2 + 1
        return min(m1, m2) + 1

