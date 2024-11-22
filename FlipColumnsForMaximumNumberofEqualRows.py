from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        val = [0] * len(matrix)
        hah1 = dict()
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                val[i] |= matrix[i][j] << j
        for i in val:
            k = min(((1 << len(matrix[0])) - 1) ^ i, i)
            hah1[k] = hah1.get(k, 0) + 1
        return max(hah1.values())