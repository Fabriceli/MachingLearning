# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-09 15:32
# @Author   : Fabrice LI
# @File     : 20191109_828_word_pattern.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a pattern and a string str, find if str follows the same pattern.
#               Here follow means a full match, such that there is a bijection between a
#               letter in pattern and a non-empty word in str.
#               You may assume pattern contains only lowercase letters,
#               and str contains lowercase letters separated by a single space.
#Reference:**********************************************
'''
E.g
Input:  pattern = "abba" and str = "dog cat cat dog"
Output: true
Explanation:
The pattern of str is abba

Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc

Input:  pattern = "aaaa" and str = "dog cat cat dog"
Output: false
Explanation:
The pattern of str is abba

Input:  pattern = "abba" and str = "dog cat cat fish"
Output: false
Explanation:
The pattern of str is abbc
'''

class Solution:
    def wordPattern(self, pattern, str):
        string = list(str.split(" "))
        if len(string) != len(pattern):
            return False
        map = {}
        for p, s in zip(pattern, string):
            if p in map.keys():
                if map[p] != s:
                    return False
            else:
                if s in map.values():
                    return False
                map[p] = s
        return True


if __name__ == '__main__':
    s = Solution()
    pattern = "abba"
    str = "dog cat cat fish"
    print(s.wordPattern(pattern, str))
