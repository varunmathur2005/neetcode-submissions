class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        cache = {} #(index, sum): BOOL

        def dfs(i, curVal):
            if (i, curVal) in cache:
                return cache[(i, curVal)]
            
            if curVal == target:
                return True

            if curVal > target or i >= len(nums):
                cache[(i, curVal)] = False
                return False
            
            cache[(i, curVal)] =  dfs(i + 1, curVal) or dfs(i + 1, curVal + nums[i])
            return cache[(i, curVal)]
        
        return dfs(0, 0)