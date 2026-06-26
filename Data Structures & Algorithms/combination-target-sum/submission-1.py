class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, curSum = [], []

        def backtrack(i, s):
            if s == target:
                res.append(curSum[:])
                return 
            if i >= n or s > target:
                return

            backtrack(i + 1, s)
            
            curSum.append(nums[i])
            backtrack(i, s + nums[i])
            curSum.pop()
            

        backtrack(0, 0)
        return res