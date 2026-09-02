class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree has n - 1 edges and no cycles
        if len(edges) != n - 1:
            return False
        
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for child in adj[node]:
                if child == par:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
        