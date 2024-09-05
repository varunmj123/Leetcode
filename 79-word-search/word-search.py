class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        col = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= col or 
            board[r][c] != word[i] or 
            (r, c) in path):
                return False
            
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or  # Down
                   dfs(r-1, c, i+1) or  # Up
                   dfs(r, c+1, i+1) or  # Right
                   dfs(r, c-1, i+1))    # Left
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(col):
                if dfs(r, c, 0): 
                    return True
        return False
