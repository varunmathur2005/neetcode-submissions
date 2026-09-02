class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        minheap = [(0, k)]
        visited = set()
        t = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for node, w in edges[n1]:
                if node not in visited:
                    heapq.heappush(minheap, (w1 + w, node))
        return t if len(visited) == n else -1
            
