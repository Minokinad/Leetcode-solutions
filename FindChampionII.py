from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        unDef = [True] * n

        for u, v in edges:
            unDef[v] = False

        chmp = -1
        chmpcnt = 0

        for team in range(n):
            if unDef[team]:
                chmp = team
                chmpcnt += 1

        if chmpcnt == 1:
            return chmp
        return -1