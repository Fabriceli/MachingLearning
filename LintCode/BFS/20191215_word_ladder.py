# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-16 00:59
# @Author   : Fabrice LI
# @File     : 20191215_word_ladder.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given two words (start and end), and a dictionary, find the shortest transformation sequence
#               from start to end, output the length of the sequence.
#               Transformation rule such that:
#
#               Only one letter can be changed at a time
#               Each intermediate word must exist in the dictionary.
#               (Start and end words do not need to appear in the dictionary )
#Reference:**********************************************
"""
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Input：start = "a"，end = "c"，dict =["a","b","c"]
Output：2
Explanation：
"a"->"c"

Input：start ="hit"，end = "cog"，dict =["hot","dot","dog","lot","log"]
Output：5
Explanation：
"hit"->"hot"->"dot"->"dog"->"cog"
"""
import collections


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict = set(dict)
        if end not in dict:
            return 0
        queue = collections.deque([start])
        result = 0
        visited = {start}

        while queue:
            size = len(queue)
            result += 1
            for _ in range(size):
                word = queue.popleft()
                if word == end:
                    return result
                for next_word in self.get_all_word(word, dict):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        return 0

    def get_all_word(self, word, dict):
        alph = "abcdefghijklmnopqrstuvwxyz"
        result = set()
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for char in alph:
                new_word = left + char + right
                if new_word in dict:
                    result.add(new_word)
        return result


if __name__ == '__main__':
    s = Solution()
    start = "hit"
    end = "cog"
    dict = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(s.ladderLength(start, end, dict))

