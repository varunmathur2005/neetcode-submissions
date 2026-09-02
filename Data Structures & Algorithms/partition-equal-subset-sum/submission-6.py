class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(target - n, -1, -1):
                if dp[i]:
                    dp[i + n] = True
                    if i + n == target:
                        return True
        
        return False