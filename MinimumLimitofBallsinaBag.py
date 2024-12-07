from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum((n - 1) // mid for n in nums) <= maxOperations: right = mid
            else: left = mid + 1
        return right