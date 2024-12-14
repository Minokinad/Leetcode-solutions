from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = len(nums)
        left = 0
        right = 0
        while left <= right < len(nums) - 1:
            st = 1
            while right < len(nums) - 1 and abs(nums[right] - nums[left]) <= 2:
                print(left, right)
                right += 1
                if abs(nums[right] - nums[left]) <= 2:
                    ans += st
                    st += 1
            while left < right and abs(nums[right] - nums[left]) > 2:
                print(left, right)
                left += 1
                if abs(nums[right] - nums[left]) <= 2:
                    ans += st
        return ans