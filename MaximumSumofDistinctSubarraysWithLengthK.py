from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = dict()
        cnt = 0
        left = 0
        cursum = 0
        ans = 0
        for i in range(0, len(nums) + 1):
            if i >= k:
                if cnt == k:
                    ans = max(ans, cursum)
                cursum -= nums[left]
                if mp[nums[left]] == 1:
                    cnt -= 1
                mp[nums[left]] -= 1
                if mp[nums[left]] == 1:
                    cnt += 1
                left += 1
            if i == len(nums):
                break
            cursum += nums[i]
            if mp.get(nums[i]) is None:
                mp[nums[i]] = 1
                cnt += 1
            else:
                if mp[nums[i]] == 1:
                    cnt -= 1
                mp[nums[i]] += 1
                if mp[nums[i]] == 1:
                    cnt += 1

        return ans
