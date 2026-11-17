class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}

        # initialize countT
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0 # Start of current window

        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            # Update Have
            if c in countT and countT[c] == window[c]:
                have += 1
            
            # Update result
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Decrement window
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""
            


        