class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        freshCount = 0
        dirs = [[1, 0],[-1, 0],[0, 1],[0, -1]]
        def inBounds(r, c):
            return (0 <= r < rows and 0 <= c < cols and 
                    grid[r][c] == 1 and (r, c) not in visited)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1
        
        time = 0
        while q and freshCount:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for ri, ci in dirs:
                    nr, nc = cr + ri, cc + ci
                    if inBounds(nr, nc):
                        visited.add((nr, nc))
                        freshCount -= 1
                        q.append((nr, nc))
            time += 1
        
        return time if freshCount == 0 else -1


