class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        def outOfBounds(r, c):
            return (r < 0 or c < 0 or r == rows or c == cols or 
                (r, c) in visit or grid[r][c] == 0
            )

        def bfs(r, c):
            area = 1
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                cr, cc = q.popleft()
                for ri, ci in dirs:
                    nr, nc = cr + ri, cc + ci
                    if not outOfBounds(nr, nc):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(res, area)
        
        return res

