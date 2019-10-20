# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-10-08 22:59
# @Author   : Fabrice LI
# @File     : 93_balanced_binary_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, determine if it is height-balanced.
#               For this problem, a height-balanced binary tree is defined
#               as a binary tree in which the depth of the two subtrees of
#               every node never differ by more than 1.
# Reference:**********************************************
'''
E.g
Input: tree = {1,2,3}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  1
		 / \
		2  3

Input: tree = {3,9,20,#,#,15,7}
	Output: true

	Explanation:
	This is a balanced binary tree.
		  3
		 / \
		9  20
		  /  \
		 15   7

Input: tree = {1,#,2,3,4}
	Output: false

	Explanation:
	This is not a balanced tree.
	The height of node 1's right sub-tree is 2 but left sub-tree is 0.
		  1
		   \
		   2
		  /  \
		 3   4
'''


# Definition of TreeNode:

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        self.res = True

        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            print(right, left)
            if abs(right - left) > 1:
                self.res = False
            return max(left, right)

        helper(root)
        return self.res
    def isBalanced2(self, root):
        return self.getDepth(root) != -1

    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        if abs(right - left) >= 2:
            return -1
        else:
            return max(right, left) + 1


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
    nums = [3,9,20,None,None,15,7]
    nums2 = [1,2,2,3,None,None,3,4,None,None,4]
    root = build(nums2)
    is_balanced = Solution().isBalanced2(root)
    print(is_balanced)
