class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = bin(num1).count('1')
        cnt2 = bin(num2).count('1')
        if cnt2 == cnt:
            return num1
        if cnt2 < cnt:
            ans = num1
            n = 0
            for i in range(cnt - cnt2):
                while 1 << n & num1 == 0:
                    n += 1
                ans -= 1 << n
                n += 1
            return ans
        ans = num1
        n = 0
        for i in range(cnt2 - cnt):
            while 1 << n & num1 != 0:
                n += 1
            ans += 1 << n
            n += 1
        return ans