# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        res = []
        if not root:
            return res
        queue.append(root)

        while queue:
            length = len(queue)
            newLayer = []
            for _ in range(length):
                node = queue.popleft()
                newLayer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(newLayer)
        
        final_result = []
        for l in res:
            final_result.append(l[-1])
    
        return final_result



