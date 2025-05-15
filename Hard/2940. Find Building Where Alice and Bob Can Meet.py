from collections import deque
from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        queries2 = []
        ans = [-1] * len(queries)
        for i in range(len(queries)):
            queries[i][0], queries[i][1] = min(queries[i][0], queries[i][1]), max(queries[i][0], queries[i][1])
            if queries[i][0] == queries[i][1] or heights[queries[i][1]] > heights[queries[i][0]]:
                ans[i] = queries[i][1]
            else:
                queries2.append([max(heights[queries[i][0]], heights[queries[i][1]]), max(queries[i][0], queries[i][1]), i])
        queries2 = sorted(queries2, key=lambda x:x[1])
        queries2 = deque(queries2)
        heap = []
        heapify(heap)
        for i in range(0, len(heights)):
            while queries2 and i == queries2[0][1]:
                heappush(heap, queries2.popleft())
            while heap and heights[i] > heap[0][0]:
                    ans[heap[0][2]] = i
                    heappop(heap)
        return ans