import copy
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxmap = [0] * 26
        wordsmap = [[0] * 26 for i in words1]
        for i in range(len(words1)):
            for j in words1[i]:
                wordsmap[i][ord(j) - 97] += 1
        print(ord('a') - 96)
        for i in words2:
            currmap = [0] * 26
            for j in i:
                currmap[ord(j) - 97] += 1
                maxmap[ord(j) - 97] = max(maxmap[ord(j) - 97], currmap[ord(j) - 97])
        ans = []
        for i in range(len(words1)):
            bol = True
            for j in range(len(maxmap)):
                if wordsmap[i][j] < maxmap[j]:
                    bol = False
                    break
            if bol:
                ans.append(words1[i])
        return ans