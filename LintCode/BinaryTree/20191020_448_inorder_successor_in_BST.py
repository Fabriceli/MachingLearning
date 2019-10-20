# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-20 23:47
# @Author   : Fabrice LI
# @File     : 20191020_448_inorder_successor_in_BST.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary search tree (See Definition) and a node in it, find the in-order
#               successor of that node in the BST.
#
#               If the given node has no in-order successor in the tree, return null.
#
#               It's guaranteed p is one node in the given tree.
#               (You can directly compare the memory address to find p)
#Reference:**********************************************
'''
E.g

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2

Input: {2,1,3}, node with value 1
Output: 2
Explanation:
    2
   / \
  1   3

Challenge
O(h), where h is the height of the BST.
'''

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor2(self, root, p):
        # situation 1 p的右子树不为空
        # 找p左最小左子树，因为是搜索二叉树，所以是最左子树
        if p.right:
            return self.minNode(p.right)
        # situation 2 p的右子树为空
        # p的后继结点是它祖先中第一个比他大的结点，也可能为空
        res = None
        while root:
            if p.val < root.val:
                res = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            elif p.val == root.val:
                break
        return res

    def inorderSuccessor(self, root, p):
        # situation 1 p的右子树不为空
        # 找p左最小左子树，因为是搜索二叉树，所以是最左子树
        if p.right:
            return self.minNode(p.right)
        # situation 2 p的右子树为空
        # p的后继结点是它祖先中第一个比他大的结点，也可能为空
        if not p.parent:
            return
        parent = p.parent
        while parent:
            if p != parent.right:
                break
            p = parent
            parent = parent.parent
        return parent


    def minNode(p):
        current = p
        while current:
            if not current.left:
                break
            current = current.left
        return current
