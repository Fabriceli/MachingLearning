# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-08 09:37
# @Author   : Fabrice LI
# @File     : 20191208_178_graph_valid_tree.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
#               write a function to check whether these edges make up a valid tree.
#Reference:**********************************************
"""
You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.

图和树的区别：n表示n个结点
1. 树的边的数=结点个数减一：n = n - 1
2. n个点联通
"""
from queue import Queue
from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = collections.defaultdict(list)
        for node, nei in edges:
            graph[node].append(nei)
            graph[nei].append(node)
        print(graph)

        queue = Queue()
        visited_set = {}
        queue.put(0)
        visited_set[0] = True
        # bfs
        while not queue.empty():
            cur = queue.get()
            for node in graph[cur]:
                print(visited_set)
                if node not in visited_set:
                    queue.put(node)
                    visited_set[node] = True
        return len(visited_set) == n


if __name__ == '__main__':
    s = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    s.validTree(n, edges)
