# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2020-01-04 14:17
# @Author   : Fabrice LI
# @File     : 20200104_602_russian_doll_envelopes.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Give a number of envelopes with widths and heights given as a pair of integers (w, h).
#               One envelope can fit into another if and only if both the width and height of one envelope
#               is greater than the width and height of the other envelope.
#               Find the maximum number of nested layers of envelopes.
# Reference:**********************************************
"""
Input：[[5,4],[6,4],[6,7],[2,3]]
Output：3
Explanation：
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Input：[[4,5],[4,6],[6,7],[2,3],[1,1]]
Output：4
Explanation：
the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
"""
from bisect import bisect_left
from typing import List


class Solution:
    """
    先排序再对第二维进行DP
    """
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]:
            return 0

        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # 转化为一位的最长上升子序列问题
        nums = []
        for e in envelopes:
            nums.append(e[1])

        # start dp
        # 定义状态
        # dp = [1 for _ in range(len(nums))]
        #
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        #
        # return max(dp)

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)


if __name__ == '__main__':
    s = Solution()
    envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    print(s.maxEnvelopes(envelopes))
