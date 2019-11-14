# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-14 20:49
# @Author   : Fabrice LI
# @File     : 20191114_114_flatten_binary_tree_to_linked_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, flatten it to a linked list in-place.
#Reference:**********************************************
'''
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:
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
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

    def dfs(self, root):
        # 递归出口
        if not root:
            return None
        # 首先要找到最后的左右结点, 为了回溯后上结点右边嵌接
        last_left = self.dfs(root.left)
        last_right = self.dfs(root.right)
        # 三部曲
        # 2. 左边接到root的右边，3. root的左边至空
        if last_left:
            # 1. 右边接到左边的右边
            last_left.right = root.right
            # 2. 左边接到root的右边
            root.right = root.left
            # 3. root的左边至空
            root.left = None

        if last_right:
            return last_right
        if last_left:
            return last_left
        return root

