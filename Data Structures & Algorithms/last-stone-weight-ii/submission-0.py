class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = (sum(stones) + 1) // 2
        cache = {}
        n = len(stones)
        def dfs(i, curWeight):
            if i == n or curWeight >= target:
                return abs(curWeight - (sum(stones) - curWeight))
            
            if (i, curWeight) in cache:
                return cache[(i, curWeight)]
            
            cache[(i, curWeight)] = min(dfs(i + 1, curWeight), 
                                        dfs(i + 1, curWeight + stones[i]))
            return cache[(i, curWeight)]
        return dfs(0, 0)