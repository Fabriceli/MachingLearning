# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-23 09:37
# @Author   : Fabrice LI
# @File     : 20191123_13_implement_strStr().py
# @User     : liyihao
# @Software : PyCharm
# @Description: For a given source string and a target string, you should output the
#               first index(from 0) of target string in source string.
#
#               If target does not exist in source, just return -1
#Reference:**********************************************
"""
Clarification:
Do I need to implement KMP Algorithm in a real interview?
Not necessary. When you meet this problem in a real interview, the interviewer may just want to test
your basic implementation ability. But make sure you confirm with the interviewer first.

E.g:
Input: source = "source" ，target = "target"
Output: -1
Explanation: If the source does not contain the target content, return - 1.

Input:source = "abcdabcdefg" ，target = "bcd"
Output: 1
Explanation: If the source contains the target content,
return the location where the target first appeared in the source.

Challenge:
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # 双指针
        if len(source) < len(target):
            return -1
        diff = len(source) - len(target) + 1
        index = 0
        while index < diff:
            if source[index:index + len(target)] == target:
                return index
            index += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    source = "sosource"
    target = "sour"
    print(s.strStr(source, target))
