class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def dfs(i, left):
            if (i, left) in cache:
                return cache[(i, left)]
            if left < 0:
                return False
            
            if i == len(s):
                return left == 0
            
            if s[i] == "(":
                cache[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ")":
                cache[(i, left)] =  dfs(i + 1, left - 1)
            else:
                cache[(i, left)] =  (dfs(i + 1, left + 1) or
                       dfs(i + 1, left - 1) or
                       dfs(i + 1, left))

            return cache[(i, left)]
        return dfs(0, 0)