class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        res = n
        # This is to find the parent of the edge
        def find(edg):
            res = edg
            while res != par[res]:
                par[res] = par[par[res]] # shorten the ll search
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res
