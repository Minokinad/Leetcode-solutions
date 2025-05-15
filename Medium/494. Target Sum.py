from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hah = dict()
        def backtrack(sm, index):
            if index == len(nums):
                if sm == target:
                    return 1
                return 0
            if hah.get((sm, index)) is not None:
                return hah[(sm, index)]
            else:
                hah[(sm, index)] = 0
            hah[(sm, index)] += backtrack(sm + nums[index], index + 1)
            hah[(sm, index)] += backtrack(sm - nums[index], index + 1)
            return hah[(sm, index)]
        return backtrack(0, 0)