class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_so_far = 0
        cache = {}

        def dfs(r, c):
            nonlocal max_so_far

            if not (0 <= r < rows and 0 <= c < cols):
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            right = dfs(r, c + 1)
            bottom_right = dfs(r + 1, c + 1)
            bottom = dfs(r + 1, c)

            if matrix[r][c] == "1":
                cache[(r, c)] = 1 + min(right, bottom_right, bottom)
                max_so_far = max(max_so_far, cache[(r, c)])
            else:
                cache[(r, c)] = 0

            return cache[(r, c)]

        dfs(0, 0)

        return max_so_far ** 2