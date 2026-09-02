class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for amt in range(amount + 1):
                if amt >= coins[i]:
                    dp[i][amt] = dp[i + 1][amt] + dp[i][amt - coins[i]]
        
        return dp[0][amount]