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
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
                
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            
        return True