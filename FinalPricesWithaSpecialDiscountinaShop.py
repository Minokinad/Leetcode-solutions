from collections import deque
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices.copy()
        prices = [(prices[i], i) for i in range(len(prices))]
        st = deque()
        for i in prices:
            while st and st[-1][0] >= i[0]:
                ans[st[-1][1]] = st[-1][0] - i[0]
                st.pop()
            st.append(i)
        return ans