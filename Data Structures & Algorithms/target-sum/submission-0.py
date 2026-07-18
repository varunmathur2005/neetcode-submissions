class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, curS):
            if i == len(nums) and curS == target:
                return 1
            if i >= len(nums):
                return 0
            
            return dfs(i + 1, curS - nums[i]) + dfs(i + 1, curS + nums[i])
        
        return dfs(0, 0)