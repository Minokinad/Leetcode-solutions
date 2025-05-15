from collections import deque, defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        deq = deque()
        ans = 0
        hah = defaultdict(list)
        deq.append((root, 0))
        while deq:
            hah[deq[0][1]].append(deq[0][0].val)
            if deq[0][0].left is not None:
                deq.append((deq[0][0].left, deq[0][1] + 1))
            if deq[0][0].right is not None:
                deq.append((deq[0][0].right, deq[0][1] + 1))
            deq.popleft()
        for i in hah:
            mas = sorted(hah[i])
            hah2 = dict()
            for j in range(len(mas)):
                hah2[mas[j]] = j
            mass = hah[i]
            for j in range(len(mas)):
                while mas[j] != mass[j]:
                    k = hah2[mass[j]]
                    mass[j], mass[k] = mass[k], mass[j]
                    ans += 1
        return ans
