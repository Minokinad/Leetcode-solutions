from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamdist(w1, w2):
            if len(w1) != len(w2):
                return False
            hm = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    hm += 1
                if hm > 1:
                    return False
            return True
        ans = [1] * len(words)
        ma, mai = 0, 0
        prev = [i for i in range(len(words))]
        for i in range(1, len(words)):
            for j in range(0, i):
                if hamdist(words[i], words[j]) and groups[i] != groups[j]:
                    if ans[i] < ans[j] + 1:
                        ans[i] = max(ans[i], ans[j] + 1)
                        if ans[i] > ma:
                            ma = ans[i]
                            mai = i
                        prev[i] = j
        a = mai
        ans2 = []
        while True:
            ans2.append(words[a])
            if a == prev[a]:
                break
            a = prev[a]
        return ans2[::-1]