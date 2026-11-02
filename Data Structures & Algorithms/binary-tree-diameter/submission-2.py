# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        record = 0
        def dfs(node):
            nonlocal record
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            record = max(record, (left + right))
            return 1 + max(left, right)
        dfs(root)
        return record
        '''Return the straight-down path, which is what your previous version did: 1 + max(left, right).
Record the bent path, left + right, in maxSum if it’s the biggest so far. You don’t return this one.
        
        
        '''
