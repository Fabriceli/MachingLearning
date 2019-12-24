# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-24 14:23
# @Author   : Fabrice LI
# @File     : 20191224_102_linked_list_cycle.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a linked list, determine if it has a cycle in it.
#Reference:**********************************************
"""
Input: 21->10->4->5,  then tail connects to node index 1(value 10).
Output: true

Input: 21->10->4->5->null
Output: false

Challenge
Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next

        while slow is not fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
