class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxlen = 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    right, b, br = dp[r][c + 1], dp[r + 1][c], dp[r + 1][c + 1]
                    dp[r][c] = 1 + min(right, b, br)
                    maxlen = max(maxlen, dp[r][c])
        
        return maxlen ** 2

    