class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen, resIndx = 0, 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                curLen = (r - l + 1)
                if curLen > maxLen:
                    maxLen = curLen
                    resIndx = l
                l, r = l - 1, r + 1

            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                curLen = (r - l + 1)
                if curLen > maxLen:
                    maxLen = curLen
                    resIndx = l
                l, r = l - 1, r + 1

        return s[resIndx: resIndx + maxLen]
