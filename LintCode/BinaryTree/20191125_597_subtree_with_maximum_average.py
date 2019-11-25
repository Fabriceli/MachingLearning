# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-25 21:40
# @Author   : Fabrice LI
# @File     : 20191125_597_subtree_with_maximum_average.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, find the subtree with maximum average. Return the root of the subtree.
#Reference:**********************************************
"""
Notice
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

Given a binary tree:

      1
    /   \
 -5     11
 / \   /  \
1   2 4    -2

return the node 11.
"""
class Solution():
    # 定义全局变量：最大和，当前node，size
    res_node = None
    res_max_sum = 0
    res_size = 0
    def findSubtree2(self, root):
        self.helper(root)
        return self.res_node

    def helper(self, root):
        # 递归的出口
        if not root:
            # 返回空结点的sum和size
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        # 当前结点的sum和size
        root_sum = left_sum + right_sum + root.val
        root_size = left_size + right_size + 1

        # 打擂台
        if self.res_max_sum == 0 or self.res_max_sum * root_size < root_sum *self.res_size:
            self.res_max_sum = root_sum
            self.res_size = root_size
            self.res_node = root
        # 返回当前结点的sum和size
        return root_sum, root_size
