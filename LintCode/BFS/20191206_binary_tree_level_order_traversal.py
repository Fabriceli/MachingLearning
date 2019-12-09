# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-06 12:45
# @Author   : Fabrice LI
# @File     : 20191206_binary_tree_level_order_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the level order traversal of its nodes' values.
#               (ie, from left to right, level by level).
# Reference:**********************************************
"""
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 层次遍历 BFS宽度优先遍历
        result = []
        if not root:
            return result
        # 创建一个队列，把起始结点放进里面（第一层结点）
        queues = [root]

        # while 队列不为空，处理队列中的结点，并扩展新的结点
        while queues:
            size = len(queues)
            cur_level = []
            # for上一层结点，并扩展下层结点
            for _ in range(size):
                #  python中list作为队列使用是需要记住FIFO，所以每次pop需要pop第一个元素，即pop(0)
                node = queues.pop(0)
                cur_level.append(node.val)
                if node.left:
                    queues.append(node.left)
                if node.right:
                    queues.append(node.right)

            result.append(cur_level)
        return result
