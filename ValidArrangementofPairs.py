from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        edges = defaultdict(list)
        inOut = defaultdict(int)

        for i in pairs:
            inOut[i[0]] += 1
            inOut[i[1]] -= 1
            edges[i[0]].append(i[1])

        start_node = pairs[0][0]
        for i in inOut:
            if inOut[i] == 1:
                start_node = i

        path = []
        def dfs(node):
            while edges[node]:
                next_node = edges[node].pop()
                dfs(next_node)
                path.append([node, next_node])

        dfs(start_node)
        return path[::-1]