class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        sp = 0
        hah = [0] * 26
        for i in s:
            hah[ord(i) - 97] = (hah[ord(i) - 97] + 1) % 2
        for i in hah:
            sp += i
        if sp <= k <= len(s):
            return True
        return False