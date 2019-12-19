# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-19 11:05
# @Author   : Fabrice LI
# @File     : 20191218_96_partition_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a linked list and a value x, partition it such that all nodes less than x come
#               before nodes greater than or equal to x.
#
#               You should preserve the original relative order of the nodes in each of the two partitions.
#Reference:**********************************************
"""
Input:  list = null, x = 0
Output: null
Explanation: The empty list Satisfy the conditions by itself.

Input:  list = 1->4->3->2->5->2->null, x = 3
Output: 1->2->2->4->3->5->null
Explanation:  keep the original relative order of the nodes in each of the two partitions.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
双子针方法，并使用dummy node
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left = left_dummy
        right = right_dummy

        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next

        left.next = right_dummy.next
        right.next = None

        return left_dummy.next
