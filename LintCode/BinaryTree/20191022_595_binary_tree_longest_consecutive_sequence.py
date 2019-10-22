# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-22 12:43
# @Author   : Fabrice LI
# @File     : 20191022_595_binary_tree_longest_consecutive_sequence.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, find the length of the longest consecutive sequence path.
#
#               The path refers to any sequence of nodes from some starting node to any node in the tree along
#               the parent-child connections. The longest consecutive path need to be from parent to child
#               (cannot be the reverse).
#Reference:**********************************************
'''
E.g
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output:3
Explanation:
Longest consecutive sequence path is 3-4-5, so return 3.

Input:
   2
    \
     3
    /
   2
  /
 1
Output:2
Explanation:
Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.
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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def __init__(self):
        self.max_len = 0
    def longestConsecutive(self, root):
        if not root:
            return 0
        def longest(node, cur_max, cur_val):
            if not node:
                return
            if node.val == cur_val + 1:
                cur_max += 1
            else:
                cur_max = 1
            self.max_len = max(cur_max, self.max_len)
            longest(node.left, cur_max, node.val)
            longest(node.right, cur_max, node.val)
        longest(root, self.max_len, root.val)
        return self.max_len
