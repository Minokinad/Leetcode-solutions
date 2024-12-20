from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = [i for i in range(len(arr))]
        for i in range(len(arr)):
            left, right = min(i, arr[i]), max(i, arr[i])
            while left > 0 and chunks[left - 1] == chunks[left]:
                left -= 1
            while right < len(chunks) - 1 and chunks[right + 1] == chunks[right]:
                right += 1
            for j in range(left, right):
                chunks[j] = right
        st = set()
        for i in chunks:
            st.add(i)
        return len(st)