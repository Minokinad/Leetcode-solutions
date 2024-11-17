from collections import deque
from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        deq = deque()
        cr = 0
        ans = float('inf')
        for i in range(len(nums)):
            cr += nums[i]
            if cr >= k:
                ans = min(ans, i + 1)
            while deq and cr - deq[0][0] >= k:
                pref, ind = deq.popleft()
                ans = min(ans, i - ind)

            while deq and deq[-1][0] >= cr:
                deq.pop()
            deq.append([cr, i])
        if ans == float('inf'):
            return -1
        return ans