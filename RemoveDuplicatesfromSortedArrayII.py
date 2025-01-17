from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = []
        ln = len(nums)
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 2] == nums[i - 1]:
                st.append(i)
                ln -= 1
            else:
                while st:
                    nums[st.pop()] = 10**5
        nums.sort()
        return ln