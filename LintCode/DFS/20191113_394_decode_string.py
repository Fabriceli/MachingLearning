# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-14 21:13
# @Author   : Fabrice LI
# @File     : 20191113_394_decode_string.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed,
# etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#Reference:**********************************************
'''
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution:
    def decodeString(self, s: str) -> str:
        return self.dfs(s, 0)

    def dfs(self, s, start_index):
        multi = 0
        res = ''
        while start_index < len(s):
            if '0' <= s[start_index] <= '9':
                multi = multi * 10 + int(s[start_index])
            elif s[start_index] == '[':
                start_index, tmp = self.dfs(s, start_index + 1)
                res += multi * tmp
                multi = 0
            elif s[start_index] == ']':
                return start_index, res
            else:
                res += s[start_index]
            start_index += 1
        return res

if __name__ == '__main__':
    s = Solution()
    st = '3[a2[c]]'
    print(s.decodeString(st))
