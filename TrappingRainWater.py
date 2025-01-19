from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, 1
        ans = 0
        while left <= right < len(height):
            temp = 0
            while left <= right < len(height) and height[left] <= height[right]:
                left += 1
                right += 1
            while left <= right < len(height) and height[left] > height[right]:
                temp += height[right]
                right += 1
            if right != len(height):
                ans += height[left] * (right - left - 1) - temp
                left = right - 1
            else:
                height = height[left:]
                height.reverse()
                left, right = 0, 1
        return ans