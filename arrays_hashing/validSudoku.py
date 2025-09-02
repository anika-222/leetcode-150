from collections import defaultdict
from typing import List

class Solution:
    #bitmasking solution O(n) space complexity because 3 arrays with 9 numbers each versus 9 sets per row, col, and square
    def validSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                val = int(board[r][c])-1 #making the integers 9-bit (0-8)
                if (1<< val) & rows[r]:
                    return False
                if (1<< val) & cols[c]:
                    return False
                if (1<<val) & squares[(r//3)*3 + c//3]:
                    return False 
                rows[r] |= (1<<val)
                cols[c] |= (1<<val)
                squares[(r//3)*3 + c//3] |= (1<<val)
        return True
    #normal hash set solution
    # def validSudoku(self, board: List[List[str]]) -> bool:
    #     rows = defaultdict(set)
    #     cols = defaultdict(set)
    #     squares = defaultdict(set)
    #     for r in range(9):
    #         for c in range(9):
    #             if board[r][c] == ".":
    #                 continue
    #             if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
    #                 return False
    #             rows[r].add(board[r][c])
    #             cols[c].add(board[r][c])
    #             squares[(r//3, c//3)].add(board[r][c])
    #     return True
    