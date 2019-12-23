# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-23 12:40
# @Author   : Fabrice LI
# @File     : 20191223_105_copy_list_with_random_pointer.py
# @User     : liyihao
# @Software : PyCharm
# @Description: A linked list is given such that each node contains an additional random pointer which
#               could point to any node in the list or null.
#
#               Return a deep copy of the list.
#Reference:**********************************************
"""
Challenge
Could you solve it with O(1) space?

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.copy_next(head)
        self.copy_random(head)
        new_node = self.split_node(head)
        return new_node

    def copy_next(self, head):
        while head:
            new_head = Node(head.val)
            new_head.random = head.random
            new_head.next = head.next
            head.next = new_head
            head = head.next.next

    def copy_random(self, head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next

    def split_node(self, head):
        new_head = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return new_head


if __name__ == '__main__':
    s = Solution()
