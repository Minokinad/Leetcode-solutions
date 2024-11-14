from typing import List
import math
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def canDistribute(k):
            if k == 0:
                return False
            ans = 0
            for i in quantities:
                ans += math.ceil(float(i) / k)
                if ans > n:
                    return False
            return True
        low = 1
        high = max(quantities)
        k = (low + high) // 2
        while not canDistribute(k) or canDistribute(k - 1) :
            if not canDistribute(k):
                low = k + 1
            else:
                high = k - 1
            k = (low + high) // 2
        return k