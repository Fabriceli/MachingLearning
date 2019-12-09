# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-07 17:45
# @Author   : Fabrice LI
# @File     : 20191205_70_binary_tree_level_order_traversal_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#               (ie, from left to right, level by level from leaf to root).
#Reference:**********************************************
"""
Input:
{1,2,3}
Output:
[[2,3],[1]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}
level order traversal

Input:
{3,9,20,#,#,15,7}
Output:
[[15,7],[9,20],[3]]
Explanation:
    3
   / \
  9  20
    /  \
   15   7
it will be serialized {3,9,20,#,#,15,7}
level order traversal
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            length = len(queue)
            cur_level = []
            for _ in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            result.append(cur_level)
        return result[::-1]

