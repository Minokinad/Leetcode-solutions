from typing import List


class Solution:
    def removeDuplicates(self, nums: List) -> int:
        st = set()
        for i in range(len(nums)):
            if nums[i] not in st:
                st.add(nums[i])
            else:
                nums[i] = 101
        st = sorted(list(st))
        for i in range(len(st)):
            nums[i] = st[i]
        return len(st)