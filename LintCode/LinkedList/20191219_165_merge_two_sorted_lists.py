# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-19 11:26
# @Author   : Fabrice LI
# @File     : 20191219_165_merge_two_sorted_lists.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Merge two sorted linked lists and return it as a new list. The new list should be made by
#               splicing together the nodes of the first two lists.
#Reference:**********************************************
"""
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
Output: 1->2->3->8->11->15->null

Input: list1 = null, list2 = 0->3->3->null
Output: 0->3->3->null
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        last_node = dummy

        while l1 and l2:
            if l1.val > l2.val:
                last_node.next = l2
                l2 = l2.next
            else:
                last_node.next = l1
                l1 = l1.next
            last_node = last_node.next

        if not l1:
            last_node.next = l2
        else:
            last_node.next = l1

        return dummy.next

