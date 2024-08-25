class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(original_node, cloned_node):
            if original_node is None:
                return None
            if original_node == target:
                return cloned_node
            left_result = dfs(original_node.left, cloned_node.left)
            if left_result:
                return left_result
            return dfs(original_node.right, cloned_node.right)
        
        return dfs(original, cloned)
