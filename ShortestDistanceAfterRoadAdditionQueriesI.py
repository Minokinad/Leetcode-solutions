from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        pref = [k for k in range(n)]
        ans = []
        hah = dict()
        for i in range(1, n):
            hah.update({i: [i - 1]})
        for u, v in queries:
            x, y = v, u
            hah[v].append(u)
            while x < n:
                for i in hah[x]:
                    pref[x] = min(pref[x], pref[i] + 1)
                x += 1
                y = x - 1
            ans.append(pref[-1])
        return ans
