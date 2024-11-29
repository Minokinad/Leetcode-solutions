from heapq import heappush
from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        directions = [(0, 1),  (1, 0), (0, -1), (-1, 0)]
        used = [[False] * len(grid[0]) for _ in range(len(grid))]
        heap = [[0,0,0]]
        heapq.heapify(heap)
        while heap:
            k, i, j = heapq.heappop(heap)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return k
            if used[i][j]:
                continue
            used[i][j] = True
            for l, m in directions:
                ni, nj = i + l, j + m
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not used[ni][nj]:
                    heapq.heappush(heap,(max(k + 1, grid[ni][nj] + abs((ni + nj) % 2 - (grid[ni][nj]) % 2)), ni, nj))
