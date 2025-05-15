from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        def dfs(root, level):
            if len(ans) <= level:
                ans.append(root.val)
            else:
                ans[level] = max(ans[level], root.val)
            if root.left is not None:
                dfs(root.left, level + 1)
            if root.right is not None:
                dfs(root.right, level + 1)
        dfs(root, 0)
        return ans