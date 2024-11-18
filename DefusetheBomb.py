from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            left = len(code) - abs(k)
        if k > 0:
            left = k
        cursum = 0
        if k < 0:
            for i in range(left, len(code)):
                cursum += code[i]
        if k > 0:
            for i in range(1, k + 1):
                cursum += code[i]
        ans = code.copy()
        for i in range(len(code)):
            if k > 0 and i != 0:
                cursum -= code[i] - code[left]
            ans[i] = cursum
            if k < 0:
                cursum += code[i] - code[left]
            left += 1
            if left == len(code):
                left = 0
        return ans