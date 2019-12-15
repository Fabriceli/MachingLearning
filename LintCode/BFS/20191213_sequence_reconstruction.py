# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-12-14 17:13
# @Author   : Fabrice LI
# @File     : 20191213_sequence_reconstruction.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
#               The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
#               Reconstruction means building a shortest common supersequence of the sequences in seqs
#               (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
#               Determine whether there is only one sequence that can be reconstructed from seqs
#               and it is the org sequence.
#Reference:**********************************************
"""
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.
---------------------------------------------------------------------------------------------
Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
---------------------------------------------------------------------------------------------
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

---------------------------------------------------------------------------------------------
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
"""
import collections
from typing import List
"""
只要保证 queue 里最多同时只有一个元素即可。
所以这是 queue 用 list 然后每次 pop 也可以，反正只有一个数。
"""

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # 1. 把图和入度构造出来
        in_degree, neighbors = self.get_in_degree(seqs)
        result = []

        # 2 标准的bfs
        queue = collections.deque([n for n in neighbors if in_degree[n] == 0])
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            result.append(node)
            for neighbor in neighbors[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) != len(neighbors):
            return False
        return result == org

    def get_in_degree(self, seqs):
        result = {}
        neighbors = {}
        for seq in seqs:
            for i in seq:
                # set 去重
                neighbors[i] = set()
                result[i] = 0
        for seq in seqs:
            for j in range(1, len(seq)):
                neighbors[seq[j - 1]].add(seq[j])

        for neighbor in neighbors:
            for j in neighbors[neighbor]:
                result[j] += 1

        return result, neighbors


if __name__ == '__main__':
    s = Solution()
    org = [4,1,5,2,6,3]
    seqs = [[5,2,6,3],[4,1,5,2]]
    print(s.sequenceReconstruction(org, seqs))
