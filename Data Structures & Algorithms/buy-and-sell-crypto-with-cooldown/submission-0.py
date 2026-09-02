class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            # We always have the option to not buy - hence cooldown
            cooldown = dfs(i + 1, buying)
            # If we can buy; i.e not (holding) or (cooldown)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cache[(i, buying)] =  max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cache[(i, buying)] = max(sell, cooldown)
            return cache[(i, buying)]

        return dfs(0, True)

