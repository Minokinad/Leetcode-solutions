from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for i in shifts:
            if i[2] == 1:
                diff[i[0]] += 1
                diff[i[1] + 1] -= 1
            else:
                diff[i[0]] -= 1
                diff[i[1] + 1] += 1
        ans = []
        for i in range(0, len(diff) - 1):
            if i != 0:
                diff[i] += diff[i - 1]
            ans.append(chr((ord(s[i]) + diff[i] + 7) % 26 + 97))
        return ''.join(ans)