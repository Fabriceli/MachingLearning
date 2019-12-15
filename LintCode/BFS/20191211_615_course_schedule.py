# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-14 09:45
# @Author   : Fabrice LI
# @File     : 20191211_615_course_schedule.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are a total of n courses you have to take, labeled from 0 to n - 1.
#
#               Some courses may have prerequisites, for example to take course 0 you have
#               to first take course 1, which is expressed as a pair: [0,1]
#
#               Given the total number of courses and a list of prerequisite pairs,
#               is it possible for you to finish all courses?
# Reference:**********************************************
"""
Input: n = 2, prerequisites = [[1,0]]
Output: true

Input: n = 2, prerequisites = [[1,0],[0,1]]
Output: false
"""
import collections
from typing import List


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites: List[List[int]]) -> bool:
        in_degree, neighbors = self.get_in_degree(numCourses, prerequistites)
        result = []
        queue = collections.deque([n for n in range(numCourses) if in_degree[n] == 0])

        while queue:
            n = queue.popleft()
            result.append(n)
            for i in neighbors[n]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        return len(result) == numCourses

    def get_in_degree(self, numCourses: int, prerequisites: List[List[int]]):
        result = {x: 0 for x in range(numCourses)}
        neighbors = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            result[j] += 1
            neighbors[i].append(j)
        return result, neighbors


if __name__ == '__main__':
    s = Solution()
    num = 2,
    prerequistites = [[1, 0]]
    print(s.canFinish(2, prerequistites))
