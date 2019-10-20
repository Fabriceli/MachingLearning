# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-11 00:00
# @Author   : Fabrice LI
# @File     : 578_lowest_common_ancestor_III.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
#               The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
#               Return null if LCA does not exist. node A or node B may not exist in tree.
#               Each node has a different value
#Reference:**********************************************
'''
E.g
Input:
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7
5 8
Output:
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

Input:
{1}
1 1
Output:
1
Explanation:
The tree is just a node, whose value is 1.
'''


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    def __init__(self):
        self.ans = None
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        def search(root):
            if not root:
                return False
            left = search(root.left)
            right = search(root.right)
            mid = root == A or root == B
            if mid + left + right >= 2:
                self.ans = root
            return mid or left or right
        search(root)
        return self.ans

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
    nums2 = [4,3,7,None,None,5,6]
    root = build(nums2)
    A = TreeNode(5)
    B = TreeNode(6)
    is_balanced = Solution().lowestCommonAncestor3(root, A, B)
    print(is_balanced)
