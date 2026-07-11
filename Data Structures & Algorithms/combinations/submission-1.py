class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, size):
            if size == k:
                res.append(sol.copy())
                return 
            
            if i > n or size > k:
                return 
            
            sol.append(i)
            backtrack(i + 1, size + 1)

            sol.pop()
            backtrack(i + 1, size)
        
        backtrack(1, 0)

        return res