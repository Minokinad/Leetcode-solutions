from collections import defaultdict
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        pref = [nums[i] % p for i in range(len(nums))]
        hah = defaultdict(int)
        for i in range(1, len(nums)):
            pref[i] = (pref[i] + pref[i - 1]) % p
        target = pref[-1]
        ans = -1
        for i in range(len(pref)):
            hah[pref[i]] = i
            if pref[i] == 0:
                if ans == -1:
                    ans = len(nums) - (hah[pref[i]] + 1)
                ans = min(ans, len(nums) - (hah[pref[i]] + 1))
                continue
            fnd = (pref[i] + p - target) % p
            if i == len(pref) - 1:
                continue
            if hah.get(fnd, None) is not None or fnd == 0:
                if ans == -1:
                    ans = abs(hah.get(fnd, -1) - hah[pref[i]])
                ans = min(ans, abs(hah.get(fnd, -1) - hah[pref[i]]))
        return ans