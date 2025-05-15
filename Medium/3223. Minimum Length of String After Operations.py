class Solution:
    def minimumLength(self, s: str) -> int:
        hah = [0] * 26
        for i in range(len(s)):
            hah[ord(s[i]) - 97] += 1
            if hah[ord(s[i]) - 97] >= 3:
                hah[ord(s[i]) - 97] -= 2
        return sum(hah)