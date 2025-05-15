from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        used = [False] * len(nums)
        numk = []
        ans = 0
        for i in range(len(nums)):
            numk.append([nums[i], i])
        numk.sort(key=lambda x: (x[0], x[1]))
        for i in numk:
            if used[i[1]]:
                continue
            used[i[1]] = True
            if i[1] > 0:
                used[i[1] - 1] = True
            if i[1] < len(nums) - 1:
                used[i[1] + 1] = True
            ans += i[0]
        return ans
