from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pref, suf = [0] * len(boxes), [0] * len(boxes)
        onp, ons = int(boxes[0]), int(boxes[-1])
        for i in range(1, len(boxes)):
            pref[i] += onp + pref[i - 1]
            suf[-i - 1] += ons + suf[-i]
            if boxes[i] == '1':
                onp += 1
            if boxes[-i - 1] == '1':
                ons += 1
        for i in range(len(boxes)):
            pref[i] += suf[i]
        return pref