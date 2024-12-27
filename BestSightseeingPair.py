from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        pref = [0] * len(values)
        suf = [0] * len(values)
        pref[0] = values[0]
        suf[-1] = values[-1] - len(values) + 1
        for i in range(1, len(values)):
            pref[i] = max(values[i] + i, pref[i - 1])
            suf[-i - 1] = max(values[-i - 1] - (len(values) - i - 1), suf[-i])
        ans = 0
        for i in range(len(values) - 2, -1, -1):
            ans = max(pref[i] + suf[i + 1], ans)
        return ans