class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left = 0
        for i in range(len(str2)):
            while left < len(str1) and str2[i] != str1[left] and str2[i] != chr((ord(str1[left]) - 96) % 26 + 97):
                  left += 1
            left += 1
        if left >= len(str1) + 1:
            return False
        else:
            return True
