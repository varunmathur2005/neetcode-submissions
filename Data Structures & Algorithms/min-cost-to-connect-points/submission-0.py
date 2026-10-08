class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = manhattan_distance(x1, y1, x2, y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        res = 0
        visit = set()
        minHeap = [(0, 0)]
        while len(visit) < n:
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            res += dist
            visit.add(point)
            for neiDist, nei in adj[point]:
                heapq.heappush(minHeap, (neiDist, nei))

        return res


