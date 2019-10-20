# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-18 00:27
# @Author   : Fabrice LI
# @File     : 68_binary_tree_postorder_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the postorder traversal of its nodes' values.
#               The first data is the root node, followed by the value of the left and right
#               son nodes, and "#" indicates that there is no child node.
#               The number of nodes does not exceed 20.
#Reference:**********************************************
'''
E.g
Input：{1,2,3}
Output：[2,3,1]
Explanation:
   1
  / \
 2   3
 it will be serialized {1,2,3}
Post order traversal

Input：{1,#,2,3}
Output：[3,2,1]
Explanation:
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
Post order traversal

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        res = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)
        postorder(root)
        return res

    def postorderTraversal_2(self, root):
        if not root:
            return []
        stack = [root,]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]

    def postorderTraversal_status(self, root):
        if not root:
            return []
        NEW = 0
        DONE = 1
        res = []
        stack = [(NEW, root)]
        while stack:
            status, node = stack.pop()
            if not node:
                continue
            if status == NEW:
                # 后序遍历：左子树 ---> 右子树 ---> 根结点
                stack.append((DONE, node))
                stack.append((NEW, node.right))
                stack.append((NEW, node.left))
                pass
            elif status == DONE:
                res.append(node.val)
        return res

