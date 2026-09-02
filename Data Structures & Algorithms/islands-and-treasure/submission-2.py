class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        water, tc, land = -1, 0, 2147483647
        q = deque()
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def inbounds(r, c):
            return (0 <= r < rows and 0 <= c < cols 
                    and grid[r][c] == land and (r, c) not in visited)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == tc:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == water:
                    visited.add((r, c))
        print(q)
        
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for ri, ci in dirs:
                    nr, nc = r + ri, c + ci
                    if inbounds(nr, nc):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        grid[nr][nc] = dist
            dist += 1


