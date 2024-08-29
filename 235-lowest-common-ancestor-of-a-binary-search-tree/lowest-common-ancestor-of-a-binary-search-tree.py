# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        high = 0
        low = 0
        if p.val > q.val:
            high = p.val
            low = q.val
        else:   
            high = q.val
            low = p.val
        if not root:
            return None
        if root and  root.val >= low and root.val <= high:
            return root
        if root.val > high:
            return self.lowestCommonAncestor(root.left, p ,q)
        if root.val < low:
            return self.lowestCommonAncestor(root.right, p ,q)

