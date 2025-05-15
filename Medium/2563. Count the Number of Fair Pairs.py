from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            k = bisect_right(nums, upper - nums[i], lo = i + 1) - 1
            e = bisect_left(nums, lower - nums[i], lo = i + 1)
            if k <= i or k >= len(nums) or e >= len(nums) or k < e:
                continue
            count += k - e + 1
        return count