class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        char = word[0]
        count = 1
        word += ' '
        for i in word[1:]:
            print(i)
            if i == char and count < 9:
                count += 1
            else:
                comp += str(count) + char
                char = i
                count = 1
        return comp