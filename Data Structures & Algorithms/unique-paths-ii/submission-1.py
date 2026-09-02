class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[rows - 1][cols - 1] == 1:
            return 0
        cache = {(rows - 1, cols - 1): 1}
        
        def dfs(i, j):            
            if i >= rows or j >= cols or grid[i][j] == 1:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            cache[(i, j)] =  dfs(i + 1, j) + dfs(i, j + 1)
            return cache[(i, j)]
        
        return dfs(0, 0)
    