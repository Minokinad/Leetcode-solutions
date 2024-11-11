from typing import List
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        hah = dict()
        prost = []
        sotprost = nums.copy()
        for i in range(1, 1100):
            for j in range(i, 1100, i):
                if i == 1:
                    hah.update({j : 1})
                else:
                    hah[j] += 1
        for i in hah.items():
            if i[1] == 2:
                prost.append(i[0])
        for i in range(len(nums) - 2, -1, -1):
            sotprost[i] = 0
            if nums[i] >= nums[i + 1]:
                print(sotprost[i])
                while nums[i] - prost[sotprost[i]] >= nums[i + 1]:
                    if nums[i] - prost[sotprost[i]] <= 0:
                        return False
                    sotprost[i] += 1
                nums[i] -= prost[sotprost[i]]
        for i in range(0, len(nums) - 1):
            if nums[i] <= nums[i + 1] and nums[i] <= 0:
                return False
        return True