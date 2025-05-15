from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        def insert(st):
            stsize = len(st)
            for k in range(j - 1, j - 1 - stsize, -1):
                box[st[-1][0]][st[-1][1]] = '.'
                st.pop()
                box[i][k] = '#'
        for i in range(len(box)):
            st = []
            for j in range(len(box[i]) + 1):
                if j == len(box[i]):
                    insert(st)
                    break
                if box[i][j] == '#':
                    st.append([i, j])
                if box[i][j] == '*':
                    insert(st)
        ans = [['.'] * len(box) for i in range(len(box[0]))]
        for j in range(len(box[0])):
            for i in range(len(box) - 1, -1, -1):
                ans[j][len(box) - (i + 1)] = box[i][j]
        return ans
