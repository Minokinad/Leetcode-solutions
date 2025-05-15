from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        start = 0
        ans = []
        for i in spaces:
            ans.append(s[start:i])
            start = i
        ans.append(s[start:])
        return ' '.join(ans)