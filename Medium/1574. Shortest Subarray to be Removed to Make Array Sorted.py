from bisect import bisect_left, bisect_right
from  typing import List
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2
        if len(arr) == 1:
            return 0
        while arr[left] >= arr[left - 1] and left < len(arr) - 1:
            left += 1
        while arr[right + 1] >= arr[right] and right > 0:
            right -= 1
        left -= 1
        right += 1
        ans = len(arr) - 1
        pref = arr[:left + 1]
        suf = arr[right:]
        for i in range(len(suf)):
            ind = bisect_right(pref, suf[i])
            print(i, ind)
            ans = min(ans, i + right - ind)
        if ans == -1:
            return 0
        ans = min(ans, len(arr) - left - 1, right)

        return ans