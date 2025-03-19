from typing import List
from collections import defaultdict


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     columns = len(board)
    #     rows = len(board[0])

    #     # checking columns
    #     for i in range(rows):
    #         checker = [0]* columns
    #         for j in range(columns):
    #             if board[i][j] != '.' and checker[j] != 0:
    #                 checker[j] = board[i][j]
    #             else:
    #                 return False
    #     # checking rows
    #     for i in range(rows):
    #         checker = [0]* rows
    #         for j in range(columns):
    #             if board[j][i] != '.' and checker[j] != 0:
    #                 checker[j] = board[i][j]
    #             else:
    #                 return False
    #     # checking in grid

    #     return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        # key = (r//3, c//3)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in columns[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True


if __name__ == "__main__":
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    assert Solution().isValidSudoku(board) is True
