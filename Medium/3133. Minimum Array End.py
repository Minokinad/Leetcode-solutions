class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        k = 0
        n -= 1
        for i in range(0, 50):
            if x & (1 << i) == 0:
                if n & (1 << k) != 0:
                    n -= 1 << k
                    ans += 1 << i
                k += 1
            if n == 0:
                break
        return ans