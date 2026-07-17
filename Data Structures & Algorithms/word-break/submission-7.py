class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in words:
                if ((i + len(w)) <= len(s) and 
                    (s[i: i + len(w)] == w)
                ):  
                    cache[i] = cache[i] or cache[i + len(w)]
        
        return cache[0]


