class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curSum = [], []
        n = len(nums)

        def backtrack(i, s):
            if s == target:
                res.append(curSum.copy())
                return
            if i == n or s > target:
                return
            
            curSum.append(nums[i])
            backtrack(i, s + nums[i])

            curSum.pop()
            backtrack(i + 1, s)

        backtrack(0, 0)
        return res
            
