# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-10-02 23:34
# @Author   : Fabrice LI
# @File     : 69_binary_tree_level_order_traversal.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a binary tree, return the level order
#               traversal of its nodes' values. (ie, from left to right, level by level).
#               The first data is the root node, followed by the value of the left and right son nodes,
#               and "#" indicates that there is no child node.
#               The number of nodes does not exceed 20.
#Reference:**********************************************
'''
E.g
Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal

Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal

Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.
'''


# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_a_Binary_Tree_by(li: List):
    if li and li[0]:
        node = TreeNode(li.pop(0))
        node.left = make_a_Binary_Tree_by(li)
        node.right = make_a_Binary_Tree_by(li)
    else:
        return li.pop(0) if li else li
    return node


class Solution:
    def levelOrder_one_queue(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root, ])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels


    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        curr_level = [root]
        res =[]
        while curr_level:
            temp = []
            next_level = []
            for i in curr_level:
                temp.append(i.val)
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            curr_level = next_level
            res.append(temp)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [3,9,20,None,None,15,7]
    root = make_a_Binary_Tree_by(nums)
    print(root)
    print(s.levelOrder_one_queue(root))

