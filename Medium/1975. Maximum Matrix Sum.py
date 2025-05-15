from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mino = float("inf")
        cnt = 0
        for i in matrix:
            for j in i:
                mino = min(mino, abs(j))
                if j < 0:
                    cnt += 1
        sm = 0
        for i in matrix:
            for j in i:
                sm += abs(j)
        if cnt % 2 == 0:
            return sm
        else:
            return sm - (2 * mino)
