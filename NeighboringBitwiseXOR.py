from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ans = 0
        for i in derived:
            ans = ans ^ i
        return ans == 0