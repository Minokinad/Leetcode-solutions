from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = nums.copy()
        ans[0] = ((1 << maximumBit) - 1) ^ nums[0]
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] ^ nums[i]
        return ans[::-1]