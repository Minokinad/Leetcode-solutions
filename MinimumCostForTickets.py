from bisect import bisect_right
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        price = [0]
        for i in range(len(days)):
            price.append(min(price[-1] + costs[0], price[bisect_right(days, days[i] - 7)] + costs[1], price[bisect_right(days, days[i] - 30)] + costs[2]))
        return price[-1]