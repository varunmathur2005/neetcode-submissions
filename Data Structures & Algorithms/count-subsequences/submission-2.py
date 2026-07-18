class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        cache = {}
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            cache[(i, j)] = res
            return res
        
        return dfs(0, 0)