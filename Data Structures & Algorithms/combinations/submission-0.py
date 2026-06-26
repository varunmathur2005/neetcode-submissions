class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, curSize):
            if curSize == k:
                res.append(sol[:])
                return
            
            if i > n or curSize > k:
                return
            
            backtrack(i + 1, curSize)

            sol.append(i)
            backtrack(i + 1, curSize + 1)
            sol.pop()
        
        backtrack(1, 0)
        return res