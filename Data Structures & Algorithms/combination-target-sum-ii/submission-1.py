class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curSum = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, s):
            if s == target:
                res.append(curSum.copy())
                return 
            
            if i == n or s > target:
                return
            
            curSum.append(candidates[i])
            backtrack(i + 1, s + candidates[i])

            curSum.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, s)

        backtrack(0, 0)
        return res 
            
