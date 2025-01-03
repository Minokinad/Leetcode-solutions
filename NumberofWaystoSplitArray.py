from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sm = sum(nums)
        smcr = 0
        ans = 0
        for i in nums[:-1]:
            smcr += i
            sm -= i
            if smcr >= sm:
                ans += 1
        return ans