class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {} # (i, j): bool
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        # dp[i][j] represents whether we can match s3'suffix using s1[:i] & s2[:j]
        # result = dp[0][0]

        # base case
        dp[n][m] = True
        
        
        for i in range(n, - 1, -1):
            for j in range(m, -1, -1):
                res = False
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
            