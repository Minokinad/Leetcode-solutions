from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = 0
        right = 0
        ans = 1
        while left <= right < len(nums) - 1:
            right += 1
            while right < len(nums) - 1 and nums[right] - nums[left] <= 2 * k:
                ans = max(ans, right - left + 1)
                right += 1
            if nums[right] - nums[left] <= 2 * k:
                ans = max(ans, right - left + 1)
            while left < right and nums[right] - nums[left] > 2 * k:
                left += 1
        return ans