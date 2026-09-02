class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[rows - 1][cols - 1] == 1 or grid[0][0] == 1:
            return 0

        grid[rows - 1][cols - 1] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    down = grid[i + 1][j] if (i + 1) < rows else 0
                    right = grid[i][j + 1] if (j + 1) < cols else 0
                    grid[i][j] = down + right
        
        return grid[0][0]
