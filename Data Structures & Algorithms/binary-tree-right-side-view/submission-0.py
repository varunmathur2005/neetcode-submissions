# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        while q:
            lastNode = None
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    lastNode = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if lastNode:
                res.append(lastNode.val)
        
        return res