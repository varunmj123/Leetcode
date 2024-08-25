class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        
        def dfs(node):
            if node is None:
                return
            if low <= node.val <= high:
                self.total += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return self.total
