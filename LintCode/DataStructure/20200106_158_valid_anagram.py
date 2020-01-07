# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2020-01-07 00:33
# @Author   : Fabrice LI
# @File     : 20200106_158_valid_anagram.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Write a method anagram(s,t) to decide if two strings are anagrams or not.
#Reference:**********************************************
"""
What is Anagram?

Two strings are anagram if they can be the same after change the order of characters.

Input: s = "ab", t = "ab"
Output: true

Input:  s = "abcd", t = "dcba"
Output: true

Input:  s = "ac", t = "ab"
Output: false

Challenge
O(n) time, O(1) extra space
"""
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = collections.defaultdict(int)

        for i in range(len(s)):
            hash_table[s[i]] = hash_table[s[i]] + 1
            hash_table[t[i]] = hash_table[t[i]] - 1
        for value in hash_table.values():
            if value:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    st = 'abcd'
    t = 'dcba'
    print(s.isAnagram(st, t))
