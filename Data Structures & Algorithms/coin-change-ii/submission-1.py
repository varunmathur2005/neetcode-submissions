class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}
        def dfs(i, curAmount):
            if curAmount == amount:
                return 1

            if i >= len(coins) or curAmount > amount:
                return 0
            
            if (i, curAmount) in cache:
                return cache[(i, curAmount)]

            c = coins[i]
            cache[(i, curAmount)] =  (dfs(i, curAmount + c) + 
                                      dfs(i + 1, curAmount)
                                    )
            return cache[(i, curAmount)]
        return dfs(0, 0)
