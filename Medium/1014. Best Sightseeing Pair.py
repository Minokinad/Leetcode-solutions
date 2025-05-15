from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, dp = 0, 0
        for i, j in enumerate(values):
            ans = max(ans, dp + j - i)
            dp = max(dp, j + i)
        return ans