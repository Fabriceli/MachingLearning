# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-14 13:54
# @Author   : Fabrice LI
# @File     : 20191212_course_schedule_II.py
# @User     : liyihao
# @Software : PyCharm
# @Description: There are a total of n courses you have to take, labeled from 0 to n-1.
#
#               Some courses may have prerequisites, for example to take course 0 you
#               have to first take course 1, which is expressed as a pair: [0,1]
#
#               Given the total number of courses and a list of prerequisite pairs,
#               return the ordering of courses you should take to finish all courses.
#
#               There may be multiple correct orders, you just need to return one of them.
#               If it is impossible to finish all courses, return an empty array.
# Reference:**********************************************
"""
Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3]


Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree, neighbors = self.get_in_degree(numCourses, prerequisites)
        result = []
        queue = collections.deque(n for n in range(numCourses) if in_degree[n] == 0)

        while queue:
            n = queue.popleft()
            result.append(n)
            for x in neighbors[n]:
                in_degree[x] -= 1
                if in_degree[x] == 0:
                    queue.append(x)
        if len(result) == numCourses:
            return result[::-1]
        else:
            return []

    def get_in_degree(self, numCourses, prerequisites):
        result = {}
        neighbors = {}
        for i in range(numCourses):
            result[i] = 0
            neighbors[i] = []
        for i, j in prerequisites:
            result[j] += 1
            neighbors[i].append(j)
        return result, neighbors


if __name__ == '__main__':
    s = Solution()
    numCourses = 3
    pre = [[0, 2], [1, 2], [2, 0]]
    print(s.findOrder(numCourses, pre))
