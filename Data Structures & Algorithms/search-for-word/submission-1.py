class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(r, c, word_match):
            if word_match == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != word[word_match] or (r, c) in visited
            ):
                return False
            
            visited.add((r, c))
            res = (dfs(r + 1, c, word_match + 1) or dfs(r, c + 1, word_match + 1) 
                    or dfs(r - 1, c, word_match + 1) or dfs(r, c - 1, word_match + 1))
            visited.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

            
            
