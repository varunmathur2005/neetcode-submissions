class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, finish in intervals[1:]:
            prevfinish = res[-1][1]
            if start <= prevfinish:
                res[-1][1] = max(prevfinish, finish)
            else:
                res.append([start, finish])
        
        return res
