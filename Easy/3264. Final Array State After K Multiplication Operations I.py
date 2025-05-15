from heapq import heapify, heapreplace
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = nums.copy()
        nums = [(nums[i], i) for i in range(len(nums))]
        heapify(nums)
        for i in range(k):
            f = nums[0]
            heapreplace(nums, (f[0] * multiplier, f[1]))
        for i,j in nums:
            ans[j] = i
        return ans