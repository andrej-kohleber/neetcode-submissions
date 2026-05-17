class Solution:
    # 00 01 02 03 04 05 06 07 08
    # 10 11 12 13 14 15 16 17 18
    # 20 21 22 23 24 25 26 27 28
    # 30 31 32 33 34 35 36 37 38
    # 40 41 42 43 44 45 46 47 48
    # 50 51 52 53 54 55 56 57 58
    # 60 61 62 63 64 65 66 67 68
    # 70 71 72 73 74 75 76 77 78
    # 80 81 82 83 84 85 86 87 88



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
            
        return True