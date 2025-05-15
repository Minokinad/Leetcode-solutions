from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2 == 0 and len(nums1) % 2 == 0:
            return 0
        if len(nums1) % 2 == 0:
            for i in nums1:
                ans ^= i
            return ans
        if len(nums2) % 2 == 0:
            for i in nums2:
                ans ^= i
            return ans
        for i in nums2:
            ans ^= i
        for i in nums1:
            ans ^= i
        return ans