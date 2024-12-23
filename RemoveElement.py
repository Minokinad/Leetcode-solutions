from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            else:
                while left < right and nums[right] == val:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return left