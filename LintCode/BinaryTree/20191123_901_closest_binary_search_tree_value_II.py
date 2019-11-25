# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-05 01:28
# @Author   : Fabrice LI
# @File     : 900_closest_binary_search_tree_value.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a non-empty binary search tree and a target value,
#               find k values in the BST that are closest to the target.
#Reference:**********************************************
'''
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

E.g
Input:
{1}
0.000000
1
Output:
[1]
Explanation：
Binary tree {1},  denote the following structure:
 1

Input:
{3,1,4,#,2}
0.275000
2
Output:
[1,2]
Explanation：
Binary tree {3,1,4,#,2},  denote the following structure:
  3
 /  \
1    4
 \
  2

Challenge
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
'''

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    # 解法1：因为是BST，所以左边结点小于右边结点，中序遍历后是一个有序的数组，中序遍历（左-根-右），
    # 中序遍历后再使用二分查找k个最接近targte的值
    def closestValue(self, root, target, k):
        if not root:
            return
        res = []
        self.inorder(root, res)
        if k >= len(res):
            return res
        index = self.binary_search(res, target)
        if index == -1:
            return
        result = []
        left = index - 1
        right = index + 1
        for i in range(k):
            result.append(res[index])
            if left >= 0 and right < len(res):
                if abs(res[left] - target) > abs(res[right] - target):
                    index = right
                    right += 1
                else:
                    index = left
                    left -= 1
            elif left >= 0:
                index = left
                left -= 1
            elif right < len(res):
                index = right
                right += 1
        return res



    # 1. 递归的定义
    def inorder(self, root, res):
        # 2. 递归的出口
        if not root:
            return
        # 3. 递归的拆解，中序遍历：左-》根-》右
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

    def binary_search(self, res, target):
        if not res:
            return -1
        left = 0
        right = len(res) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if res[mid] == target:
                return mid
            elif res[mid] > target:
                right = mid
            elif res[mid] < target:
                left = mid
        if abs(res[left] - target) > abs(res[right] - target):
            return right
        else:
            return left


    # 解法2：在中序遍历过程中比较root.val和target的大小，当res里面还没有k个值时，都将val放进res里面
    def closestValue_v2(self, root, target, k):
        if not root:
            return
        res = []
        self.inorder_v2(root, target, k, res)
        return res

    def inorder_v2(self, root, target, k, res):
        if not root:
            return
        self.inorder_v2(root.left, target, k, res)
        if len(res) < k:
            res.append(root.val)
        elif abs(root.val - target) < abs(res[0] - target):
            res.pop(0)
            res.append(root.val)
        else:
            return
        self.inorder_v2(root.right, target, k, res)

    def inorderTraversal(self, root):
        if not root:
            return []
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res


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
    nums2 = [4,2,5,1,3]
    root = build(nums2)
    target = 3.7
    k = 2
    is_balanced = Solution().closestValue(root, target, k)
    print(is_balanced)
    print(Solution().inorderTraversal(root))
    print(Solution().closestValue_v2(root, target, k))


