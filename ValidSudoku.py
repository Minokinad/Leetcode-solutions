from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st1 = [set() for _ in range(9)]
        st2 = [set() for _ in range(9)]
        st3 = [set() for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if board[i][j] in st1[i] or board[i][j] in st2[j] or board[i][j] in st3[i // 3 * 3 + j // 3]:
                        return False
                    st1[i].add(board[i][j])
                    st2[j].add(board[i][j])
                    st3[i // 3 * 3 + j // 3].add(board[i][j])
        return True