from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        reps = [[0] * len(words[0]) for _ in range(len(target))]
        for i in range(len(target)):
            for j in range(len(words)):
                for k in range(i, len(words[0]) - len(target) + i + 1):
                    if target[i] == words[j][k]:
                        reps[i][k] += 1
        for i in range(len(target)):
            for k in range(1, len(words[0])):
                if i == 0:
                    reps[i][k] += reps[i][k - 1]
                else:
                    reps[i][k] = (reps[i][k - 1] + reps[i][k] * reps[i - 1][k - 1]) % (10 ** 9 + 7)
        return reps[-1][-1]