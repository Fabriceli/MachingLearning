# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-07 22:01
# @Author   : Fabrice LI
# @File     : 20191204_71_binary_tree_zigzag_level_order_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the zigzag level order traversal of its nodes' values.
#               (ie, from left to right, then right to left for the next level and alternate between).
#Reference:**********************************************
"""
Input:{1,2,3}
Output:[[1],[3,2]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}

Input:{3,9,20,#,#,15,7}
Output:[[3],[20,9],[15,7]]
Explanation:
    3
   / \
  9  20
    /  \
   15   7
it will be serialized {3,9,20,#,#,15,7}
"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result
        queues = [root]
        left_to_right = False
        while queues:
            length = len(queues)
            cur_level = []
            for _ in range(length):
                node = queues.pop(0)
                if node.left:
                    queues.append(node.left)
                if node.right:
                    queues.append(node.right)
                cur_level.append(node.val)
            # 根据层数判断是从右起还是从左起
            if left_to_right:
                result.append(cur_level[::-1])
            else:
                result.append(cur_level)
            left_to_right = not left_to_right
        return result

