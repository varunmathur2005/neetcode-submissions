class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[i][j] : true if using the first i elements we can form sum j

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                # if the current number in nums is <= the jth value
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1]
