from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pref = [0]
        for i in range(len(words)):
            pref.append(pref[-1])
            if words[i][-1] in 'aeiou' and words[i][0] in 'aeiou':
                pref[-1] += 1
        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = pref[queries[i][1] + 1] - pref[queries[i][0]]
        return ans