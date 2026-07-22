class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            adj[u].append([v, values[i]])
            adj[v].append([u, 1/values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q = deque([(src, 1)])
            visited = set()
            visited.add(src)
            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                
                for nei, weight in adj[node]:
                    if nei not in visited:
                        q.append([nei, w * weight])
                        visited.add(nei)

            return -1
        
        return [bfs(u,v) for u, v in queries]