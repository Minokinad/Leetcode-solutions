from collections import defaultdict


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        s = ''.join(sorted(s))
        hah = defaultdict(int)
        for i in s:
            hah[i] += 1
        ans = ''
        clz = list(hah.keys())
        while len(clz) > 0:
            ans += clz[-1] * min(repeatLimit, hah[clz[-1]])
            hah[clz[-1]] -= min(repeatLimit, hah[clz[-1]])
            if hah[clz[-1]] <= 0:
                clz.pop()
            else:
                if len(clz) > 1:
                    ans += clz[-2]
                    hah[clz[-2]] -= 1
                    if hah[clz[-2]] == 0:
                        clz.pop(-2)
                else:
                    break
        return ans