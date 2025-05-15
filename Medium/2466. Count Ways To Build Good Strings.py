class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]
        ans = 0
        for i in range(1, high + 1):
            if len(dp) == i:
                dp.append(0)
            if i == zero:
                dp[i] = (dp[i] + 1) % (10**9 + 7)
            if i == one:
                dp[i] = (dp[i] + 1) % (10**9 + 7)
            if i > zero:
                dp[i] = (dp[i] + dp[i - zero]) % (10**9 + 7)
            if i > one:
                dp[i] = (dp[i] + dp[i - one]) % (10**9 + 7)
            if i >= low:
                ans = (ans + dp[i]) % (10**9 + 7)

        return ans