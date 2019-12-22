# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-19 11:45
# @Author   : Fabrice LI
# @File     : 20191220_36_reverse_linked_list_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Reverse a linked list from position m to n.
#               Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.
# Reference:**********************************************
"""
Input: 1->2->3->4->5->NULL, m = 2 and n = 4,
Output: 1->4->3->2->5->NULL.

Input: 1->2->3->4->NULL, m = 2 and n = 3,
Output: 1->3->2->4->NULL.

Challenge
Reverse it in-place and in one-pass
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # 记录m的pre和mth结点
        mth_pre = self.find_k_th(dummy, m - 1)
        mth = mth_pre.next
        # 记录n和n.next结点
        nth = self.find_k_th(dummy, n)
        nth_next = nth.next
        nth.next = None

        # 翻转结点
        self.reverse(mth)

        # 处理m-n的头和尾
        mth_pre.next = nth
        mth.next = nth_next

        return dummy.next

    def find_k_th(self, head, k):
        for _ in range(k):
            head = head.next
            if not head:
                return None
        return head

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
