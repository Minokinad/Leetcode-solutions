from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pref = [1] * len(nums)
        ans = []
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                pref[i] += pref[i - 1]
        for i, j in queries:
            if pref[j] - pref[i] == j - i:
                ans.append(True)
            else:
                ans.append(False)
        return ans