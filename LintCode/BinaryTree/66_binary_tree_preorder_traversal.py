# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-20 23:28
# @Author   : Fabrice LI
# @File     : 66_binary_tree_preorder_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the preorder traversal of its nodes' values.
#
#               The first data is the root node, followed by the value of the left and
#               right son nodes, and "#" indicates that there is no child node.
#               The number of nodes does not exceed 20.
#Reference:**********************************************
'''
E.g

Input：{1,2,3}
Output：[1,2,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Preorder traversal

Input：{1,#,2,3}
Output：[1,2,3]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Preorder traversal

Challenge
Can you do it without recursion?

前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点

层次遍历：只需按层次遍历即可
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res

    def preorderTraversalNonRecu(self, root):
        if not root:
            return []
        NEW = 1
        DONE = 0
        stack = [(NEW, root)]
        res = []
        while stack:
            status, node = stack.pop()
            if not node:
                continue
            if status == NEW:
                # 前序遍历 根 - 左 - 右
                stack.append((DONE, node))
                stack.append((NEW, node.left))
                stack.append((NEW, node.right))
            elif status == DONE:
                res.append(node.val)
        return res
