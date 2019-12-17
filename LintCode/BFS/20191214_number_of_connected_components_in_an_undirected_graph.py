# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-15 23:54
# @Author   : Fabrice LI
# @File     : 20191214_number_of_connected_components_in_an_undirected_graph.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
#               write a function to find the number of connected components in an undirected graph.
#Reference:**********************************************
"""
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

"""
import collections
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        # 1. create graph
        graph = {i: set() for i in range(n)}
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        print(graph)
        visited = set()
        result = 0

        for i in range(n):
            if i not in visited:
                self.bfs(i, graph, visited)
                result += 1
        return result

    def bfs(self, i, graph, visited):
        queue = collections.deque([i])
        while queue:
            x = queue.popleft()
            for j in graph[x]:
                if j not in visited:
                    queue.append(j)
                    visited.add(j)


if __name__ == '__main__':
    s = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]] # [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(s.countComponents(n, edges))
