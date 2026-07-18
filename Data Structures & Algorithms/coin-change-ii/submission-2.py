class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # dp[i][j] represents no of way to get amount j using index i onwards
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i + 1][j]
                if coins[i] <= j:
                    dp[i][j] += dp[i][j - coins[i]]

        return dp[0][amount]
