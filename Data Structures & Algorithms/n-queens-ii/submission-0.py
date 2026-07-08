class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [["."] * n for _ in range(n)]
        colSet = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in colSet or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                colSet.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                colSet.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res


            