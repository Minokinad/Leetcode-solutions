from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ans = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        deq = deque()
        deq.append((0, 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans[0][0] = 0
        while len(deq) != 0:
            i, j = deq.popleft()
            for l, m in directions:
                ni, nj = i + l, j + m
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and ans[ni][nj] > ans[i][j] + grid[ni][nj]:
                    ans[ni][nj] = ans[i][j] + grid[ni][nj]
                    if grid[ni][nj] == 0:
                        deq.appendleft((ni, nj))
                    else:
                        deq.append((ni, nj))
        return int(ans[-1][-1])