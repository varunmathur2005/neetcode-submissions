class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {} # (i, j): bool
        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            
            if j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            
            cache[(i, j)] = res

            return cache[(i, j)]
        
        return dfs(0, 0, 0)
            