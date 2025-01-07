from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        words = sorted(words, key=lambda x: len(x))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans