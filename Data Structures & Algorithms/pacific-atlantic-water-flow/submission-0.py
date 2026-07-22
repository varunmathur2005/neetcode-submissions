class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(heights), len(heights[0])
        res = []
        def dfs(r, c, visit, curE):
            visit.add((r, c))
            for ri, ci in dirs:
                nr, nc = r + ri, c + ci
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visit and curE <= heights[nr][nc]
                ):
                    visit.add((nr, nc))
                    dfs(nr, nc, visit, heights[nr][nc])
                
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        
        return res


