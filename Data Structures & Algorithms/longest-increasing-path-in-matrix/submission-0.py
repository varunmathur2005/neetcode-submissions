class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        cache = {}
        def outOfBounds(r, c, cur):
            return not(0 <= r < rows and 0 <= c < cols and matrix[r][c] > cur)
        
        def dfs(r, c, prev):
            if outOfBounds(r, c, prev):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            res = 1
            for ri, ci in dirs:
                nr, nc = r + ri, c + ci
                res = max(res, 1 + dfs(r + ri, c + ci, matrix[r][c]))
            cache[(r, c)] = res
            return res
            
        LIP = 0
        for r in range(rows):
            for c in range(cols):
                LIP = max(dfs(r, c, float("-inf")), LIP)
        
        return LIP
        

            
