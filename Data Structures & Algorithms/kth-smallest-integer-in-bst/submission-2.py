# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        cnt = k
        result = root.val

        def dfs(node) -> int:
            nonlocal cnt, result
            
            if not node:
                return

            dfs(node.left)
            if cnt == 0:
                return

            cnt -= 1
            if cnt == 0:
                result = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return result

            