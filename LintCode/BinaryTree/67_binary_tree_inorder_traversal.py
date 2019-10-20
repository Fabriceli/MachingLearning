# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-10-20 00:33
# @Author   : Fabrice LI
# @File     : 67_binary_tree_inorder_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the inorder traversal of its nodes' values.
# Reference:**********************************************
'''
E.g
Input：{1,2,3}
Output：[2,1,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Inorder Traversal

Input：{1,#,2,3}
Output：[1,3,2]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Inorder Traversal

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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        if not root:
            return []
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def inorderTraversalNonRecu(self, root):
        if not root:
            return []
        GRAY = 1  # 已访问
        GREEN = 0  # 新节点
        res = []
        stack = [(GREEN, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == GREEN:
                stack.append((GREEN, node.right))
                stack.append((GRAY, node))
                stack.append((GREEN, node.left))
            elif color == GRAY:
                res.append(node.val)
        return res

