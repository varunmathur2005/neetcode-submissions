class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        We store the index of each characters last occurance
        So, when we see a char is repeating we can update l to remove
        the repetition.
        Now, there are 2 cases:
        char being repeated is ahead of l:
            In this case we can just move l to repeat char index + 1
        char being repeated is behind l:
            We can keep l as it is
        '''
        map_index = {}
        l = 0
        res = 0
        for r, c in enumerate(s):
            if c in map_index:
                l = max(l, map_index[c] + 1) # Always move l ahead
            map_index[c] = r
            res = max(res, r - l + 1)
        
        return res