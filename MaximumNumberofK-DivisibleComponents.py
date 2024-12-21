from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        hah = defaultdict(list)
        for i in edges:
            hah[i[0]].append(i[1])
            hah[i[1]].append(i[0])
        def tree(root):
            for i in hah[root]:
                hah[i].remove(root)
                tree(i)
        tree(0)
        print(hah)
        for i in range(n):
            values[i] %= k
        def dfs(root, par):
            if len(hah[root]) != 0:
                for i in hah[root]:
                    values[root] = (values[root] + dfs(i, root)) % k
            else:
                if values[root] % k == 0:
                    pass
            return values[root] % k
        dfs(0, 0)
        ans = 0
        for i in range(n):
            if values[i] == 0:
                ans += 1
        return ans