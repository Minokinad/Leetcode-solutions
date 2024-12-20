from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = []
        def rec(node, lvl):
            if len(stk) == lvl // 2:
                stk.append([])
            if lvl % 2 == 1:
                stk[lvl // 2].append(node)
            if node.left is not None:
                rec(node.left, lvl + 1)
                rec(node.right, lvl + 1)
        rec(root, 0)
        for i in stk:
            for j in range(len(i) // 2):
                i[j].val, i[-(j + 1)].val = i[-(j + 1)].val, i[j].val
        return root