class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(lpar, rpar):
            if lpar == rpar == n:
                res.append("".join(sol[:]))
                return
            
            if lpar < n:
                sol.append("(")
                backtrack(lpar + 1, rpar)
                sol.pop()
            if rpar < lpar:
                sol.append(")")
                backtrack(lpar, rpar + 1)
                sol.pop()
        
        backtrack(0, 0)
        return res
        
