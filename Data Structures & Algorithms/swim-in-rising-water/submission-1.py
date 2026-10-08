class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def inbounds(r, c):
            return (0 <= r < rows and 0 <= c < cols and (r, c) not in visit)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if (r, c) == (rows - 1, cols - 1):
                return height
            if (r, c) in visit:
                continue
            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not inbounds(nr, nc):
                    continue
                new_height = grid[nr][nc]
                max_height = max(height, new_height)
                heapq.heappush(minHeap, (max_height, nr, nc))
        

            
            

