class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        left = -1
        right = -1
        hah1 = dict()
        hah1.update({'a': 0})
        hah1.update({'b': 0})
        hah1.update({'c': 0})
        for i in s:
            hah1[i] += 1
        ans = float('inf')
        while left <= right < len(s) - 1:
            while right < len(s) - 1 and hah1['a'] >= k and hah1['b'] >= k and hah1['c'] >= k:
                ans = min(ans, len(s) - (right - left))
                right += 1
                hah1[s[right]] -= 1
            if hah1['a'] >= k and hah1['b'] >= k and hah1['c'] >= k:
                ans = min(ans, len(s) - (right - left))
            while (left <= right and left < len(s)) and (hah1['a'] < k or hah1['b'] < k or hah1['c'] < k):
                left += 1
                hah1[s[left]] += 1

        if ans == float('inf'):
            return -1
        return ans