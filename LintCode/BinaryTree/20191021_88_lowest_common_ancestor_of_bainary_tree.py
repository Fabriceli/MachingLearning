# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-21 21:03
# @Author   : Fabrice LI
# @File     : 20191021_88_lowest_common_ancestor_of_bainary_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given the root and two nodes in a Binary Tree.
#               Find the lowest common ancestor(LCA) of the two nodes.
#
#               The lowest common ancestor is the node with largest depth
#               which is the ancestor of both nodes.
#Reference:**********************************************
'''
E.g
Input：{1},1,1
Output：1
Explanation：
 For the following binary tree（only one node）:
         1
 LCA(1,1) = 1

 Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
 For the following binary tree:

      4
     / \
    3   7
       / \
      5   6

 LCA(3, 5) = 4
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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
