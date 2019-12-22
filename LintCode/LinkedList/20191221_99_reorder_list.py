# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-21 19:59
# @Author   : Fabrice LI
# @File     : 20191221_99_reorder_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a singly linked list L: L0 → L1 → … → Ln-1 → Ln
#
#               reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# Reference:**********************************************
"""
Example 1:
	Input:  1->2->3->4->null
	Output: 1->4->2->3->null

Example 2:
	Input: 1->2->3->4->5->null
	Output: 1->5->2->4->3->null

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None

        # 2. reverse
        second = None
        while middle:
            temp = middle.next
            middle.next = second
            second = middle
            middle = temp

        # 3. merge
        dummy = ListNode(0)
        last_node = dummy

        index = 1
        while head and second:
            if index % 2:
                last_node.next = head
                head = head.next
            else:
                last_node.next = second
                second = second.next
            last_node = last_node.next
            index += 1

        if not head:
            last_node.next = second
        else:
            last_node.next = head

        return dummy.next


    def find_middle(self, head: ListNode):
        # 快慢指针方式求中点，慢指针1一个单位速度，快指针2个单位速度，
        # 快指针走完刚好是慢指针走了一半
        slow = head
        fast = head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):

        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp

        return pre

    def merge(self, head, second):
        dummy = ListNode(0)
        last_node = dummy

        index = 1
        while head and second:
            if index // 2:
                last_node.next = head
                head = head.next
            else:
                last_node.next = second
                second = second.next
            last_node = last_node.next
            index += 1

        if not head:
            last_node.next = second
        else:
            last_node.next = head

if __name__ == '__main__':
    s = Solution()
    a5 = ListNode(5)
    a5.next = None
    a4 = ListNode(4)
    a4.next = a5
    a3 = ListNode(3)
    a3.next = a4
    a2 = ListNode(2)
    a2.next = a3
    head = ListNode(1)
    head.next = a2
    # pre = head
    # while pre:
    #     print(pre.val)
    #     pre = pre.next
    s.reorderList(head)
