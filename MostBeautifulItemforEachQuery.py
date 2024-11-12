from bisect import bisect_left
from typing import List
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])
        mas = [0]
        hah = {0: 0}
        for i in items:
            if mas[len(mas) - 1] != i[0]:
                mas.append(i[0])
                hah.update({i[0]: 0})
            hah[i[0]] = max(hah[i[0]], hah[mas[len(mas) - 2]], i[1])
        ans = []
        for i in queries:
            if hah.get(i, -1) != -1:
                ans.append(hah.get(i))
                continue
            ans.append(hah.get(mas[bisect_left(mas, i) - 1]))
        return ans