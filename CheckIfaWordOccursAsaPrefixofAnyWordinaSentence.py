class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wrds = sentence.split(" ")
        for i in range(len(wrds)):
            if wrds[i].startswith(searchWord):
                return i + 1
        return -1