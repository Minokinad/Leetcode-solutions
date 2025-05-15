import heapq
from typing import List


class Solution:
    def trapRainWater(self, heights: List[List[int]]) -> int:
        heap = []
        total = 0
        if len(heights) == 1 or len(heights[0]) == 1:
            return 0
        visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(heights)):
            visited[i][0] = True
            heapq.heappush(heap, [heights[i][0], i, 0])
            visited[i][-1] = True
            heapq.heappush(heap, [heights[i][-1], i, len(heights[0]) - 1])
        for i in range(1, len(heights[0]) - 1):
            visited[0][i] = True
            heapq.heappush(heap, [heights[0][i], 0, i])
            visited[-1][i] = True
            heapq.heappush(heap, [heights[-1][i], len(heights) - 1, i])
        while heap:
            k, i, j = heapq.heappop(heap)
            for m, l in directions:
                ni, nj = i + m, j + l
                if 0 <= ni < len(heights) and 0 <= nj < len(heights[0]):
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        if heights[ni][nj] < k:
                            total += k - heights[ni][nj]
                        heapq.heappush(heap, [max(heights[ni][nj], k), ni, nj])
        return total
