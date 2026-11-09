class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])

        def inbounds(r, c):
            return (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited)

        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if not inbounds(nr, nc):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    

        for r in range(rows):
            for c in range(cols):
                if inbounds(r, c):
                    bfs(r, c)
                    count += 1
        
        return count