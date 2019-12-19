# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-18 23:53
# @Author   : Fabrice LI
# @File     : 20191217_450_reverse_nodes_in_k-Group.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
#               If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
#               You may not alter the values in the nodes, only nodes itself may be changed.
#               Only constant memory is allowed.
#Reference:**********************************************
"""
Input:
list = 1->2->3->4->5->null
k = 2
Output:
2->1->4->3->5

Input:
list = 1->2->3->4->5->null
k = 3
Output:
3->2->1->4->5
"""

# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy

        while pre:
            pre = self.reverse(pre, k)

        return dummy.next

    def reverse(self, head, k):
        # find k node
        cur = head
        n1 = head.next
        for i in range(k):
            if not cur:
                return None
            cur = cur.next

        if not cur:
            return None

        # reverse
        nk = cur
        nkplus = cur.next

        pre = head
        cur = head.next
        while cur != nkplus:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        # for head and tail
        n1.next = nkplus
        head.next = nk

        return n1

