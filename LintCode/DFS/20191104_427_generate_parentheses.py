# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-04 18:09
# @Author   : Fabrice LI
# @File     : 20191104_427_generate_parentheses.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given n, and there are n pairs of parentheses, write a function to generate all
#               combinations of well-formed parentheses.
#Reference:**********************************************
'''
E.g
Input: 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Input: 2
Output: ["()()", "(())"]


做“回溯”算法问题的基本套路是：

1、使用题目中给出的示例，画树形结构图，以便分析出递归结构；

一般来说，树形图不用画完，就能够分析出递归结构和解题思路。

2、分析一个结点可以产生枝叶的条件、递归到哪里终止、是否可以剪枝、符合题意的结果在什么地方出现（可能在叶子结点，也可能在中间的结点）；

3、完成以上两步以后，就要编写代码实现上述分析的过程，使用代码在画出的树形结构上搜索符合题意的结果。

在树形结构上搜索结果集，使用的方法是执行一次“深度优先遍历”。在遍历的过程中，可能需要使用“状态变量”。
'''

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        if not n or n <= 0:
            return []
        res = []
        # 减法
        # self.dfs("", n, n, res)
        # 加法
        self.dfs_add("", 0, 0, n, res)
        return res

    # 做减法
    def dfs(self, s, left, right, res):
        if left == 0 and right == 0:
            res.append(s)
            return
        if left > 0:
            self.dfs(s + "(", left - 1, right, res)
        if left < right and right > 0:
            self.dfs(s + ")", left, right - 1, res)

    # 做加法
    def dfs_add(self, s, left, right, n, res):
        if left == n and right == n:
            res.append(s)
            return
        if left <= n:
            self.dfs_add(s + "(", left + 1, right, n, res)

        if left > right <= n:
            self.dfs_add(s + ")", left, right + 1, n, res)


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.generateParenthesis(3))
