from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        dct = defaultdict(int)
        dct[s[0]] += 1
        st = 1
        ans = -1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                st = 1
                dct[s[i]] += 1
                if dct[s[i]] >= 3 and ans == -1:
                    ans = 1
                continue
            st += 1
            a = s[i]
            for i in range(st):
                dct[a] += 1
                if dct[a] >= 3 and len(a) > ans:
                    ans = len(a)
                a += s[i]
        return ans