from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        dop = nums[n - k:] + nums[:n - k]
        for i in range(n):
            nums[i] = dop[i]