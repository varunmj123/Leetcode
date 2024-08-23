# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left: 
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)  # Assign the result back to root.right
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)  # Assign the result back to root.left
        else: 
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else: 
                minimumNode = self.minNode(root.right) 
                root.val = minimumNode.val
                root.right = self.deleteNode(root.right, minimumNode.val)

        return root
