class Solution:
    def canBeValid(self, s: str, l: str) -> bool:
        if len(s) % 2 != 0:
            return False
        opnInd, unlcdInd = [], []
        for i in range(len(s)):
            if l[i] == '0':
                unlcdInd.append(i)
            if l[i] == '1':
                if s[i] == '(':
                    opnInd.append(i)
                if s[i] == ')':
                    if opnInd:
                        opnInd.pop()
                    elif unlcdInd:
                        unlcdInd.pop()
                    else:
                        return False
        while opnInd:
            if not unlcdInd:
                return False
            if unlcdInd.pop() < opnInd.pop():
                return False
        return True
