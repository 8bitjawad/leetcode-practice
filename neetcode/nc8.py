class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box_index = (r // 3) * 3 + (c // 3)

                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True




        # for i in range(9):
        #     new_set = set()
        #     for j in range(9):
        #         if board[i][j] not in new_set:
        #             if board[i][j] != ".":
        #                 new_set.add(board[i][j])
        #         else:
        #             return False
                

        # for i in range(9):
        #     new_set = set()
        #     for j in range(9):
        #         if board[j][i] not in new_set:
        #             if board[j][i] != ".":
        #                 new_set.add(board[j][i])
        #         else:
        #             return False

        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         new_set = set()
        #         for r in range(i,i+3):
        #             for c in range(j,j+3):
        #                 if board[r][c] not in new_set:
        #                     if board[r][c] != ".":
        #                         new_set.add(board[r][c])
        #                 else:
        #                     return False

        # return True





        