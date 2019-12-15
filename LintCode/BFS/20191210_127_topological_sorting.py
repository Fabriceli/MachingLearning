# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-14 09:22
# @Author   : Fabrice LI
# @File     : 20191210_127_topological_sorting.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given an directed graph, a topological order of the graph nodes is defined as follow:
#
#               For each directed edge A -> B in graph, A must before B in the order list.
#               The first node in the order can be any node in the graph with no nodes direct to it.
#               Find any topological order for the given graph.
#
#               You can assume that there is at least one topological order in the graph.
#Reference:**********************************************
"""
https://www.lintcode.com/problem/topological-sorting/description

"""
import collections

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        if not graph:
            return []
        in_degree = self.get_in_degree(graph)

        queue = collections.deque([node for node in graph if in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    def get_in_degree(self, graph):
        result = {x: 0 for x in graph}
        for node in graph:
            for neighbor in node.neighbors:
                result[neighbor] += 1
        return result
