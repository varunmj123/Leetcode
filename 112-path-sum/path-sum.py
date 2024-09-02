class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def backtrack(node, current_sum):
            if not node:
                return False
            current_sum += node.val

            if not node.left and not node.right and current_sum == targetSum:
                return True

            left = backtrack(node.left, current_sum)
            right = backtrack(node.right, current_sum)

            current_sum -= node.val
            
            return left or right


        return backtrack(root, 0)
