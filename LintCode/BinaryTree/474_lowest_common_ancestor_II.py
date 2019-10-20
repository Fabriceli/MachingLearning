# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-15 01:13
# @Author   : Fabrice LI
# @File     : 474_lowest_common_ancestor_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
#
#               The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
#
#               The node has an extra attribute parent which point to the father of itself. The root's parent is null.
#Reference:**********************************************
'''
E.g
Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
     4
     / \
    3   7
       / \
      5   6
LCA(3, 5) = 4

Input：{4,3,7,#,#,5,6},5,6
Output：7
Explanation：
      4
     / \
    3   7
       / \
      5   6
LCA(5, 6) = 7
'''
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        li = []
        while A:
            li.append(A)
            A = A.parent
        while B:
            if B in li:
                return B
            B = B.parent
        return None

