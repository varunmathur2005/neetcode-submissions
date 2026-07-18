class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, curS):
            if i == len(nums):
                return 1 if curS == target else 0

            if (i, curS) in cache:
                return cache[(i, curS)]
            
            cache[(i, curS)] = dfs(i + 1, curS - nums[i]) + dfs(i + 1, curS + nums[i])
            return cache[(i, curS)]
        
        return dfs(0, 0)