# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        nodeMax = root.val
        self.output = 0
        def dfs(root, nodeMax):
            if not root:
                return 
            if root.val >= nodeMax:
                nodeMax = root.val
                self.output +=1
            
            dfs(root.left, nodeMax)
            dfs(root.right, nodeMax)
        dfs(root, nodeMax)
        return self.output 
                