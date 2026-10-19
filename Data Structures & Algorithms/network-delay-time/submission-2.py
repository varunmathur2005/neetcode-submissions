class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for src, target, time in times:
            edges[src].append([time, target])      

        minHeap = [[0, k]]
        visited = set()
        time = 0
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            time = t
            for t_nei, nei in edges[node]:
                if nei in visited:
                    continue
                heapq.heappush(minHeap, [t_nei + time, nei])

        return time if len(visited) == n else -1

            
