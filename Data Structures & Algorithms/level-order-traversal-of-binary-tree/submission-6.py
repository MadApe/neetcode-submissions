# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)

        levels = [[root.val, ], ]

        while q:
            current_level = list()
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    current_level.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    current_level.append(node.right.val)
                    q.append(node.right)

            if len(current_level) > 0: 
                levels.append(current_level)

        return levels
            