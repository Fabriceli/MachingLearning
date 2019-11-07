# -*-coding:utf-8 -*-
#Reference:**********************************************
# @Time     : 2019-11-07 23:40
# @Author   : Fabrice LI
# @File     : 20191107_123_word_search.py
# @User     : liyihao
# @Software : PyCharm
# @Description: Given a 2D board and a word, find if the word exists in the grid.
#
#               The word can be constructed from letters of sequentially adjacent cell,
#               where "adjacent" cells are those horizontally or vertically neighboring.
#               The same letter cell may not be used more than once.
#Reference:**********************************************
'''
E.g
Input：["ABCE","SFCS","ADEE"]，"ABCCED"
Output：true
Explanation：
[
     A B C E
     S F C S
     A D E E
]
(0,0)A->(0,1)B->(0,2)C->(1,2)C->(2,2)E->(2,1)D

Input：["z"]，"z"
Output：true
Explanation：
[ z ]
(0,0)z
'''
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    # 方向数组
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    def exist(self, board, word):
        row = len(board)
        if not row:
            return False
        column = len(board[0])
        dp = [[0 for _ in range(column)] for _ in range(row)]
        for r in range(row):
            for c in range(column):
                if self.found_word(board, word, 0, r, c, dp, row, column):
                    return True
        return False

    def found_word(self, board, word, index, cur_row, cur_column, dp, row, column):
        if index == len(word) - 1:
            return board[cur_row][cur_column] == word[index]
        if board[cur_row][cur_column] == word[index]:
            dp[cur_row][cur_column] = 1
            for d in self.direction:
                new_row = cur_row + d[0]
                new_column = cur_column + d[1]
                if 0 <= new_row < row \
                        and 0 <= new_column < column \
                        and not dp[new_row][new_column] \
                        and self.found_word(board, word, index + 1, new_row, new_column, dp, row, column):
                    return True
            dp[cur_row][cur_column] = 0
        return False


if __name__ == '__main__':
    s = Solution()
    board = ["ABCE", "SFCS", "ADEE"]
    word = "ABCCED"
    print(s.exist(board, word))
