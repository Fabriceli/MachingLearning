# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-08 00:23
# @Author   : Fabrice LI
# @File     : 453_flatten_binary_tree to_linked_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Flatten a binary tree to a fake "linked list" in pre-order traversal.
#
#               Here we use the right pointer in TreeNode as the next pointer in ListNode.
#Reference:**********************************************
'''
E.g
Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6

Input:{1}
Output:{1}
Explanation：
         1
         1

Challenge
Do it in-place without any extra memory.
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if not root:
            return root
        while root:
            if root.left:
                to_right = root.left
                while to_right.right:
                    to_right = to_right.right
                to_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
