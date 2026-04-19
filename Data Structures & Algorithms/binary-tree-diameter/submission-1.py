# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.diameter