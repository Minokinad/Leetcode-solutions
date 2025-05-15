from typing import List


class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        c = [0] * len(b)
        st1, st2 = set(), set()
        for i in range(len(a)):
            st1.add(a[i])
            st2.add(b[i])
            c[i] = len(st1 & st2)
        return c