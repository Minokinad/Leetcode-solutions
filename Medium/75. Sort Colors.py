from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        st, en = 0, len(nums) - 1
        while nums[st] == 0 and st < en:
            st += 1
        while nums[en] == 2 and en > st:
            en -= 1
        i = st
        while st <= i <= en:
            if nums[i] == 0:
                nums[st], nums[i] = nums[i], nums[st]
                st += 1
            if nums[i] == 2:
                nums[en], nums[i] = nums[i], nums[en]
                en -= 1
                continue
            i += 1