class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(lparen, rparen):
            if rparen == n:
                res.append("".join(sol.copy()))
                return 
            
            if lparen < n:
                sol.append("(")
                backtrack(lparen + 1, rparen)
                sol.pop()
            
            if rparen < lparen:
                sol.append(")")
                backtrack(lparen, rparen + 1)
                sol.pop()
        backtrack(0, 0)
        return res