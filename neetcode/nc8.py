class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            new_set = set()
            for j in range(9):
                if board[i][j] not in new_set:
                    if board[i][j] != ".":
                        new_set.add(board[i][j])
                else:
                    return False
                

        for i in range(9):
            new_set = set()
            for j in range(9):
                if board[j][i] not in new_set:
                    if board[j][i] != ".":
                        new_set.add(board[j][i])
                else:
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                new_set = set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] not in new_set:
                            if board[r][c] != ".":
                                new_set.add(board[r][c])
                        else:
                            return False

        return True





        