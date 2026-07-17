class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 1}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            cache[i] = dfs(i - 3) + dfs(i - 2) + dfs(i - 1)
            
            return cache[i]
        
        return dfs(n)
        