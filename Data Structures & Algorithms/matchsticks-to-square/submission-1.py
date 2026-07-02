class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        
        used = [False] * len(matchsticks)

        def backtrack(i, k, curSum):
            if k == 0:
                return True
            
            if curSum == length:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(matchsticks)):
                if not used[j] and curSum + matchsticks[j] <= length:
                    used[j] = True
                    if backtrack(j + 1, k, curSum + matchsticks[j]):
                        return True
                    used[j] = False
                
            return False
        
        return backtrack(0, 4, 0)