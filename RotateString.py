class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for j in range(len(s) + 1):
            print(s)
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False