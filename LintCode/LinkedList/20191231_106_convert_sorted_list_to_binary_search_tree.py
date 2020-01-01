# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-31 19:53
# @Author   : Fabrice LI
# @File     : 20191231_106_convert_sorted_list_to_binary_search_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a singly linked list where elements are sorted in ascending order,
#               convert it to a height balanced BST.
# Reference:**********************************************
"""
Example 1:
	Input: array = 1->2->3
	Output:
		 2
		/ \
	   1   3

Example 2:
	Input: 2->3->6->7
	Output:
		 3
		/ \
	   2   6
		    \
		     7

	Explanation:
	There may be multi answers, and you could return any of them.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        def find_mid(head):
            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next =None
            return slow

        mid = find_mid(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
