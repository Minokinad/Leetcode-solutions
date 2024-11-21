from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ans = []
        for i in range(m):
            ans.append([0] * n)
        for guard in guards:
            ans[guard[0]][guard[1]] = 2
        for wall in walls:
            ans[wall[0]][wall[1]] = 3
        for i in range(m):
            st = []
            met = False
            for j in range(n):
                if ans[i][j] == 0:
                    st.append([i, j])
                if ans[i][j] == 2:
                    met = True
                    for k, z in st:
                        ans[k][z] = 1
                    st.clear()
                if ans[i][j] == 3:
                    if met:
                        met = False
                        for k, z in st:
                            ans[k][z] = 1
                    st.clear()
            if met:
                for k, z in st:
                    ans[k][z] = 1

        for i in range(n):
            st = []
            met = False
            for j in range(m):
                if ans[j][i] == 0:
                    st.append([j, i])
                if ans[j][i] == 2:
                    met = True
                    for k, z in st:
                        ans[k][z] = 1
                    st.clear()
                if ans[j][i] == 3:
                    if met:
                        met = False
                        for k, z in st:
                            ans[k][z] = 1
                    st.clear()
            if met:
                for k, z in st:
                    ans[k][z] = 1
        ans2 = 0
        for i in ans:
            for j in i:
                if j == 0:
                    ans2 += 1
        return ans2
