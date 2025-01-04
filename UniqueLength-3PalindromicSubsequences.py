from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hah = defaultdict(list)
        hah2 = defaultdict(set)
        for i in range(len(s)):
            hah[s[i]].append(i)
        st = set()
        for i in range(len(s)):
            if s[i] not in st and i != hah[s[i]][-1]:
                for j in st:
                    hah2[j].add(s[i])
                st.add(s[i])
                continue
            elif s[i] in st and i == hah[s[i]][-1]:
                st.remove(s[i])
            for j in st:
                hah2[j].add(s[i])
        ans = 0
        for i in hah2.keys():
            ans += len(hah2[i])
        return ans