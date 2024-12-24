from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def bfs(adjacency_list, start):
            distances = {v: -1 for v in adjacency_list}
            distances[start] = 0
            queue = deque([start])
            while queue:
                current = queue.popleft()
                for neighbor in adjacency_list[current]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)
            return distances
        def diameter(adjacency_list):
            v, u, w = 0, 0, 0
            n = len(adjacency_list)
            d = bfs(adjacency_list, v)
            for i in range(n):
                if d[i] > d[u]:
                    u = i
            d = bfs(adjacency_list, u)
            for i in range(n):
                if d[i] > d[w]:
                    w = i
            return d[w]
        adjacency_list1 = defaultdict(list)
        for u, v in edges1:
            adjacency_list1[u].append(v)
            adjacency_list1[v].append(u)
        adjacency_list2 = defaultdict(list)
        for u, v in edges2:
            adjacency_list2[u].append(v)
            adjacency_list2[v].append(u)
        d1 = diameter(adjacency_list1)
        d2 = diameter(adjacency_list2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
