# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-22 12:33
# @Author   : Fabrice LI
# @File     : 20191222_170_rotate_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a list, rotate the list to the right by k places, where k is non-negative.
# Reference:**********************************************
"""
Input:1->2->3->4->5  k = 2
Output:4->5->1->2->3

Input:3->2->1  k = 1
Output:1->3->2

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # find list node size
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next

        k = k % size
        if k == 0:
            return head

        # find k node
        k = size - k
        kth = head
        for _ in range(k - 1):
            kth = kth.next

        new_head = kth.next
        kth.next = None

        # find new tail
        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head

        return new_head


if __name__ == '__main__':
    s = Solution()
