from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        hah = dict()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hah[mat[i][j]] = (i, j)
        rows, cols = [0] * len(mat), [0] * len(mat[0])
        for j, i in enumerate(arr):
            rows[hah[i][0]] += 1
            cols[hah[i][1]] += 1
            if rows[hah[i][0]] >= len(mat[0]) or cols[hah[i][1]] >= len(mat):
                return j