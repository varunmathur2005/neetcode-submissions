class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        subsetSum = sum(nums) // k
        used = [False] * len(nums)
        nums.sort(reverse=True)
        def backtrack(i, k, curSum):
            if k == 0:
                return True
            
            if curSum == subsetSum:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if not used[j] and curSum + nums[j] <= subsetSum:
                    used[j] = True
                    if backtrack(j + 1, k, curSum + nums[j]):
                        return True
                    used[j] = False
            
            return False

        return backtrack(0, k, 0)

