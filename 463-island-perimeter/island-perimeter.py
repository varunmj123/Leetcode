class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        total = 0
        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] == 0):
                return 0
            if grid[r][c] == 1:
                return 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                    covered = 0
                    for dr, dc in directions:
                        covered += dfs(r + dr,c + dc)
                    total += (4 - covered)
        return total

                    
        