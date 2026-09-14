class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if grid[rows - 1][cols - 1] == 1 or grid[0][0] == 1:
            return -1

        dirs = [
            [1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, -1],
            [1, -1], [-1, 1]
        ]

        visited = set()
        q = deque()
        q.append([0, 0, 1])
        visited.add((0, 0))
        min_path = float('inf')
        def inbounds(r, c):
            return (0 <= r < rows and
                        0 <= c < cols and
                        (r, c) not in visited and
                        grid[r][c] == 0)
        
        while q:
            r, c, cur_path = q.popleft()
            if r == rows - 1 and c == cols - 1:
                return cur_path
            for ri, ci in dirs:
                nr, nc = r + ri, c + ci
                if inbounds(nr, nc):
                    q.append([nr, nc, cur_path + 1])
                    visited.add((nr, nc))
        return -1