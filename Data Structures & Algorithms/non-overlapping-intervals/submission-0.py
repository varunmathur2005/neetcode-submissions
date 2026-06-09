class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prevI = intervals[0]

        for start, end in intervals[1:]:
            if start < prevI[1]:
                res += 1
                prevI = [start, min(end, prevI[1])]
            else:
                prevI = [start, end]
        
        return res
