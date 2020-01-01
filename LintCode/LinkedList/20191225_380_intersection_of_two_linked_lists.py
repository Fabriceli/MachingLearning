# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-25 11:05
# @Author   : Fabrice LI
# @File     : 20191225_380_intersection_of_two_linked_lists.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Write a program to find the node at which the intersection of two singly linked lists begins.
#Reference:**********************************************
"""
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.

Input:
	A:          a1 → a2
	                   ↘
	                     c1 → c2 → c3
	                   ↗
	B:     b1 → b2 → b3
Output: c1
Explanation ：begin to intersect at node c1.

Input:
Intersected at 6
1->2->3->4->5->6->7->8->9->10->11->12->13->null
6->7->8->9->10->11->12->13->null
Output: Intersected at 6
Explanation：begin to intersect at node 6.

Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            if not pa:
                pa = headB
            else:
                pa = pa.next
            if not pb:
                pb = headA
            else:
                pb = pb.next
        return pa

    def getIntersectionNode_v0(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        size_a = self.get_length(headA)
        size_b = self.get_length(headB)
        diff = size_a - size_b
        if diff > 0:
            for _ in range(diff):
                headA = headA.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None
        else:
            diff = abs(diff)
            for _ in range(diff):
                headB = headB.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None


    def get_length(self, head):
        size = 1
        while head:
            size += 1
            head = head.next
        return size
