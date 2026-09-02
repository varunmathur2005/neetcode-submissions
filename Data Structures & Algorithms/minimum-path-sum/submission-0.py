class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cache = {
            (rows - 1, cols - 1): grid[rows - 1][cols - 1]
        }
        def dfs(i, j):
            if i >= rows or j >= cols:
                return float("inf")
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            cache[(i, j)] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return cache[(i, j)]
    

        return dfs(0, 0)
