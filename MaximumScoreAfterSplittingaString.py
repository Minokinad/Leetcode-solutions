class Solution:
    def maxScore(self, s: str) -> int:
        suf = [int(s[-1])] * len(s)
        pref = [abs(int(s[0])-1)] * len(s)

        for i in range(1, len(s)):
            pref[i] = pref[i - 1] + abs(int(s[i]) - 1)
            suf[-i - 1] = suf[-i] + int(s[-i - 1])

        ans = 0
        for i in range(len(s) - 1):
            ans = max(pref[i] + suf[i + 1], ans)
        return ans