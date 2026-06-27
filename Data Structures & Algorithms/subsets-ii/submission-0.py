class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res

