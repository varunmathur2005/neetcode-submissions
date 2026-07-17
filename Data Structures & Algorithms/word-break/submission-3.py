class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            for w in wordDict:
                if ((i + len(w) <= len(s)) 
                    and (s[i: i + len(w)] == w)
                ):
                    if dfs(i + len(w)):
                        cache[i] = True
                        return cache[i]
            
            cache[i] = False
            return False
    
        return dfs(0)

