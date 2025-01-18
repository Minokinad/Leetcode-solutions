from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp =[[10**5] * m for _ in range(n)]
        dp[0][0] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        deq = deque([(0, 0)])
        while deq:
            i, j = deq.popleft()
            ni, nj = i + directions[grid[i][j] - 1][0], j + directions[grid[i][j] - 1][1]
            if 0 <= ni < n and 0 <= nj < m and dp[ni][nj] > dp[i][j]:
                dp[ni][nj] = dp[i][j]
                deq.appendleft((ni, nj))
            for k, l in directions:
                ni, nj = i + k, j + l
                if 0 <= ni < n and 0 <= nj < m and dp[ni][nj] > dp[i][j] + 1:
                    dp[ni][nj] = dp[i][j] + 1
                    deq.append((ni, nj))
        return dp[-1][-1]
