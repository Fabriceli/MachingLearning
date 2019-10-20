# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-09 23:06
# @Author   : Fabrice LI
# @File     : 902_kth_smallest_element_in_a_BST.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary search tree, write a function
#               kthSmallest to find the kth smallest element in it.
#               You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#Reference:**********************************************
'''
E.g
Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.

Challenge
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        if not root:
            return 0
        stack = [(1, root)]
        while stack:
            a, node = stack.pop()
            if a == 0:
                k -= 1
                if k == 0:
                    return node.val
            else:
                if node.right:
                    stack.append((1, node.right))
                stack.append((0, node))
                if node.left:
                    stack.append((1, node.left))


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
    nums2 = [3,1,4,None,2]
    root = build(nums2)
    k = 3
    is_balanced = Solution().kthSmallest(root, k)
    print(is_balanced)
