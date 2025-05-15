from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * (len(nums) - k + 1)
        m = 1
        if k == 1:
            for i in range(len(ans)):
                ans[i] = nums[i]
            return ans
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                m += 1
            else:
                m = 1
            if m >= k:
                ans[i + 1 - k] = nums[i]
        return ans