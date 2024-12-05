class Solution:
    def canChange(self, s: str, t: str) -> bool:
        i, j = 0, 0
        s, t = s + ' ', t + ' '
        while i < len(s) or j < len(s):
            while i < len(s) and s[i] == '_': i += 1
            while j < len(s) and t[j] == '_': j += 1
            if s[i] != t[j]: return False
            if s[i] == 'L' and i < j: return False
            if s[i] == 'R' and i > j: return False
            i, j = i + 1, j + 1
        return True