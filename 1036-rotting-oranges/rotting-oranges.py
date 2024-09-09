class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        rotLoc = {}
        freshLoc = {}
        q = deque()
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    freshLoc[(r,c)] = (r,c)
                if grid[r][c] == 2:
                    rotLoc[(r,c)] = (r,c)
        for r , c in rotLoc.keys():
            q.append((r,c))

        def bfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r,c) not in freshLoc
                or grid[r][c] == 0
            ):
                return 0 

            if (r,c) in freshLoc:
                del freshLoc[(r,c)]
                q.append((r,c))
                return 1
        while q:
            temp = 0
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0 , -1]]
                for dr,dc in directions:
                    temp  += bfs(r + dr, c + dc)
            if temp > 0:
                time +=1
        if freshLoc:
            return -1
        return time