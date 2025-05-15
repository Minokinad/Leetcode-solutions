from typing import Optional,List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for j in candidates:
                if j & (1 << i) != 0:
                    cnt += 1
            ans = max(ans, cnt)
        return ans