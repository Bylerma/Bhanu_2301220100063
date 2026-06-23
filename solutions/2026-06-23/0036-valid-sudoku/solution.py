# Number: 0036
# Title: Valid Sudoku
# Difficulty: Medium
# Tags: Array, Hash Table, Matrix
# Language: Python3
# URL: https://leetcode.com/problems/valid-sudoku/
# Date: 2026-06-23
# Runtime: 0 ms (Beats 96.78%)
# Memory: N/A

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):  
                ch = board[i][j]
                
                if ch != '.':  
                    board[i][j] = '.' 
                    
                    if not self.isValid(board, ch, i, j): 
                        return False 
                    
                    board[i][j] = ch 
                    
        return True

    def isValid(self, ch_matrix: list[list[str]], ch1: str, i: int, j: int) -> bool:
        for k in range(9):
            
            if ch_matrix[i][k] == ch1:
                return False
            
            if ch_matrix[k][j] == ch1:
                return False
            
            row_idx = 3 * (i // 3) + k // 3
            col_idx = 3 * (j // 3) + k % 3
            if ch_matrix[row_idx][col_idx] == ch1:
                return False
                
        return True