from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        ind = groups[0]
        for i in range(1, len(groups)):
            if ind != groups[i]:
                ans.append(words[i])
                ind = groups[i]
        return ans
