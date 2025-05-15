from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[0])

        suff = [0] * len(events)
        suff[len(events) - 1] = events[-1][2]

        for i in range(len(events) - 2, -1, -1):
            suff[i] = max(events[i][2], suff[i + 1])

        maxSum = 0

        for i in range(len(events)):
            left, right = i + 1, len(events) - 1
            nextEvent = -1

            while left <= right:
                mid = left + (right - left) // 2
                if events[mid][0] > events[i][1]:
                    nextEvent = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if nextEvent != -1:
                maxSum = max(maxSum, events[i][2] + suff[nextEvent])

            maxSum = max(maxSum, events[i][2])

        return maxSum