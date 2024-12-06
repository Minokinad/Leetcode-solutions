from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = sorted(banned)
        sm, ans = 0, 0
        i = 1
        for i in range(1, n + 1):
            if sm + i > maxSum:
                return ans
            if len(banned) == 0 or i != banned[0]:
                ans += 1
                sm += i
            while len(banned) > 0 and i == banned[0]:
                banned.pop(0)

        return ans