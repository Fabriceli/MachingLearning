# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-24 14:44
# @Author   : Fabrice LI
# @File     : 20191224_103_linked_list_cycle_ii.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a linked list, return the node where the cycle begins.
#
#               If there is no cycle, return null.
#Reference:**********************************************
"""
Input：null,no cycle
Output：no cycle
Explanation：
List is null，so no cycle.

Input：-21->10->4->5，tail connects to node index 1
Output：10
Explanation：
The last node 5 points to the node whose index is 1, which is 10, so the entrance of the ring is 10

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Challenge
Follow up:

Can you solve it without using extra space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
1. 使用双指针判断链表中是否有环，慢指针每次走一步，快指针每次走两步，若链表中有环，则两指针必定相遇。

2. 假设环的长度为l，环上入口距离链表头距离为a，两指针第一次相遇处距离环入口为b，则另一段环的长度为c=l-b，
    由于快指针走过的距离是慢指针的两倍，则有a+l+b=2*(a+b),又有l=b+c，可得a=c，故当判断有环时(slow==fast)时，
    移动头指针，同时移动慢指针，两指针相遇处即为环的入口。
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head.next

        while slow is not fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
