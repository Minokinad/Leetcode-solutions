from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [[-((x[0] + 1) / (x[1] + 1) - x[0] / x[1]), x] for x in classes]
        heapify(classes)
        for i in range(1, extraStudents + 1):
            clas = heappop(classes)
            x, h = clas[1][0] + 1, clas[1][1] + 1
            clas = [-((x + 1) / (h + 1) - x / h), [x, h]]
            heappush(classes, clas)
        return sum(i[1][0] / i[1][1] for i in classes) / len(classes)