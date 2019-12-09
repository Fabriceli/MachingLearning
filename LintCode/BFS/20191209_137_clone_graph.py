# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019-12-09 20:30
# @Author   : Fabrice LI
# @File     : 20191209_137_clone_graph.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#               Nodes are labeled uniquely.
#
#               You need to return a deep copied graph, which has the same structure as the original graph,
#               and any changes to the new graph will not have any effect on the original graph.
#
#               You need return the node with the same label as the input node.
# Reference:**********************************************
"""
Input:
{1,2,4#2,1,4#4,1,2}
Output:
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2
 \     |
  \    |
   \   |
    \  |
      4

Graph
For example:

{1,2,4#2,1,4#3,5#4,1,2#5,3} represents follow graph:

1------2  3
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      4   5
we use # to split each node information.
1,2,4 represents that 2, 4 are 1's neighbors
2,1,4 represents that 1, 4 are 2's neighbors
3,5 represents that 5 is 3's neighbor
4,1,2 represents that 1, 2 are 4's neighbors
5,3 represents that 3 is 5's neighbor
"""
import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
"""


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        """
        1. 从原图给定的点找到所有点
        2. 复制所有的点
        3. 复制所有的边
        """
        if not node:
            return node
        root = node
        # 1. use bfs to get all points
        nodes = self.get_all_nodes(node)

        # 2. deep copy all points
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        print(mapping)

        # 3. deep copy all edges
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]


    # bfs
    def get_all_nodes(self, node):
        queue = collections.deque([node])
        result = set([node])
        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result


if __name__ == '__main__':
    s = Solution()
    node = []
    s.cloneGraph(node)
