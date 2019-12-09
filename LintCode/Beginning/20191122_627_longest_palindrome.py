# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-23 00:34
# @Author   : Fabrice LI
# @File     : 20191122_627_longest_palindrome.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a string which consists of lowercase or uppercase letters,
#               find the length of the longest palindromes that can be built with those letters.
#
#               This is case sensitive, for example "Aa" is not considered a palindrome here.
#
#               Note:
#               Assume the length of given string will not exceed 1,010.
#Reference:**********************************************
"""
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    """
    hashmap 对应 python是set，
    一个set和一个count
    遍历整个字符串，已存在set的的字符remove，并且count + 2；不存在的add进set
    """
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        res = set()
        count = 0
        for string in s:
            if string in res:
                res.remove(string)
                count += 2
            else:
                res.add(string)
        if len(res) <= 0:
            return count
        return count + 1


    def longestPalindrome2(self, s: str) -> int:
        if not s:
            return 0
        d = set()
        for c in s:
            if c in d:
                d.remove(c)
            else:
                d.add(c)
        return len(s) if not d else len(s) - len(d) + 1


if __name__ == '__main__':
    s = Solution()
    string = "ababababa"
    print(s.longestPalindrome(string))
