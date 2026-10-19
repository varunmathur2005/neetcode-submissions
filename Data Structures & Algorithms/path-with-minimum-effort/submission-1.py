class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        def can_visit(r, c):
            return 0 <= r < rows and 0 <= c < cols and (r, c) not in visit
        
        minheap = [[0, 0, 0]] # diff, r, c

        while minheap:
            diff, r, c = heapq.heappop(minheap)
            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            if (r, c) in visit: continue
            
            visit.add((r, c))
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not can_visit(nr, nc):
                    continue
                newdiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minheap, [newdiff, nr, nc])
        
