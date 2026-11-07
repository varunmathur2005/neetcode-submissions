class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return None

            left = dfs(node.left)
            if left is not None:
                return left

            k -= 1
            if k == 0:
                return node.val

            return dfs(node.right)

        return dfs(root)