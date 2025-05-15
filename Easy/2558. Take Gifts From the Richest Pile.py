from math import sqrt
from typing import List
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hp = [-x for x in gifts]
        heapq.heapify(hp)
        for i in range(k):
            heapq.heappush(hp, -int(sqrt(-heapq.heappop(hp))))
        return -sum(hp)