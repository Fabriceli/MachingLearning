# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-30 19:42
# @Author   : Fabrice LI
# @File     : 20191230_98_sort_list.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Sort a linked list in O(n log n) time using constant space complexity.
#Reference:**********************************************
"""
Input:  1->3->2->null
Output:  1->2->3->null

Input: 1->7->2->6->null
Output: 1->2->6->7->null

Challenge
Solve it by merge sort & quick sort separately.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# merge sort: nlogn, space: o(n) for array, o(1) for linked list
# quick sort: nlogn, space: o(1) fro all
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # def merge(right, left):
        #     dummy = ListNode(0)
        #     head = dummy
        #
        #     while left and right:
        #         if left.val > right.val:
        #             head.next = right
        #             right = right.next
        #         else:
        #             head.next = left
        #             left = left.next
        #         head = head.next
        #     if left:
        #         head.next = left
        #     else:
        #         head.next = right
        #
        #     return dummy.next
        #
        # fast = head
        # slow = head
        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # mid = slow.next
        # slow.next = None

        mid = self.find_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.merge(right, left)

    def find_mid(self, head):
        if not head:
            return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(self, right, left):
        dummy = ListNode(0)
        head = dummy

        while left and right:
            if left.val > right.val:
                head.next = right
                right = right.next
            else:
                head.next = left
                left = left.next
            head = head.next
        if left:
            head.next = left
        else:
            head.next = right

        return dummy.next

if __name__ == '__main__':
    s = Solution()
    #  [4,2,1,3]
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    result = s.sortList(head)
    while result:
        print(result.val)
        result = result.next
