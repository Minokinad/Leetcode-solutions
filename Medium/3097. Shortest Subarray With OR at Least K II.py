from typing import  List
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        curor = 0
        minlength = len(nums)
        hah = dict()
        for i in range(0, 33):
            hah.update({i:0})
        s = (bin(nums[0])[2:])[::-1]
        for i in range(len(s)):
            if s[i] == '1':
                hah[i] += 1
                curor |= (1 << i)
        maxor = curor
        if curor >= k:
            return 1
        while right < len(nums) - 1 or (curor >= k and left < right):
            while right < len(nums) - 1:
                right += 1
                s = (bin(nums[right])[2:])[::-1]
                for i in range(len(s)):
                    if s[i] == '1':
                        hah[i] += 1
                        if hah[i] == 1:
                            curor |= (1 << i)
                maxor = max(maxor, curor)
                if curor >= k:
                    print(minlength)
                    minlength = min(minlength, right - left + 1)
                    break
            while curor >= k and left < right:
                s = (bin(nums[left])[2:])[::-1]
                for i in range(len(s)):
                    if s[i] == '1':
                        hah[i] -= 1
                        if hah[i] == 0:
                            curor ^= (1 << i)
                left += 1
                if curor >= k:
                    print(minlength)
                    minlength = min(minlength, right - left + 1)
        if maxor < k:
            return -1
        return minlength