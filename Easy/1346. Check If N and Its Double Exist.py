from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        st = set()
        zero = False
        for i in range(len(arr)):
            if arr[i] == 0 and not zero:
                zero = True
                continue
            elif arr[i] == 0:
                return True
            st.add(arr[i])
            st.add(arr[i] * 2)
            if len(st) % 2 == 1:
                return True
        return False