class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for indx, interval in enumerate(intervals):
            curS, curE = interval
            if curE < newInterval[0]:
                res.append(interval)
            elif curS > newInterval[1]:
                res.append(newInterval)
                return res + intervals[indx:]
            else:
                newInterval = [min(curS, newInterval[0]), max(curE, newInterval[1])]
        res.append(newInterval)
        return res
