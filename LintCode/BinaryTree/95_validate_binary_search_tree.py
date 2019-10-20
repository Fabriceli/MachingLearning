# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-10-11 23:58
# @Author   : Fabrice LI
# @File     : 95_validate_binary_search_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, determine if it is a valid binary search tree (BST).
#
#               Assume a BST is defined as follows:
#
#               - The left subtree of a node contains only nodes with keys less than the node's key.
#               - The right subtree of a node contains only nodes with keys greater than the node's key.
#               - Both the left and right subtrees must also be binary search trees.
#               - A single node tree is a BST
# Reference:**********************************************
'''
E.g
Input:  {-1}
Output：true
Explanation：
For the following binary tree（only one node）:
	      -1
This is a binary search tree.

Input:  {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res == sorted(res) and len(res) == len(set(res))


# 创建二叉树
def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root


if __name__ == "__main__":
    nums = [3, 9, 20, None, None, 15, 7]
    nums2 = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    root = build(nums)
    is_balanced = Solution().isValidBST(root)
    print(is_balanced)
